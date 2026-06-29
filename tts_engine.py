import os
import re
import asyncio
import subprocess
from dotenv import load_dotenv

load_dotenv()

VOICE = os.getenv('TTS_VOICE', 'es-ES-ElviraNeural')
MAX_CHARS = 5000


def chunk_text(text):
    paragraphs = re.split(r'\n\s*\n', text)
    chunks = []

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        if len(para) <= MAX_CHARS:
            chunks.append(para)
        else:
            sentences = re.split(r'(?<=[.!?])\s+', para)
            current = ''
            for sentence in sentences:
                if len(current) + len(sentence) + 1 <= MAX_CHARS:
                    current += sentence + ' '
                else:
                    if current:
                        chunks.append(current.strip())
                    if len(sentence) > MAX_CHARS:
                        for i in range(0, len(sentence), MAX_CHARS):
                            chunks.append(sentence[i:i + MAX_CHARS].strip())
                    else:
                        current = sentence + ' '
            if current:
                chunks.append(current.strip())

    return chunks


async def _process(task_id, filepath, output_dir, tasks):
    import edge_tts

    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    chunks = chunk_text(text)
    total_chars = sum(len(c) for c in chunks)
    chars_done = 0
    temp_files = []

    for i, chunk in enumerate(chunks):
        temp_path = os.path.join(output_dir, f'{task_id}_chunk_{i}.mp3')
        temp_files.append(temp_path)

        communicate = edge_tts.Communicate(chunk, VOICE, boundary="WordBoundary")
        words_total = max(len(chunk.split()), 1)
        words_done = 0

        with open(temp_path, 'wb') as f:
            async for event in communicate.stream():
                if event['type'] == 'audio':
                    f.write(event['data'])
                elif event['type'] == 'WordBoundary':
                    words_done += 1
                    chunk_progress = words_done / words_total
                    total_progress = ((chars_done + chunk_progress * len(chunk)) / max(total_chars, 1)) * 80
                    tasks[task_id]['progress'] = round(min(total_progress, 80.0), 2)

        chars_done += len(chunk)
        tasks[task_id]['progress'] = round((chars_done / max(total_chars, 1)) * 80, 2)

    tasks[task_id]['progress'] = 85

    list_path = os.path.join(output_dir, f'{task_id}_list.txt')
    with open(list_path, 'w', encoding='utf-8') as f:
        for tf in temp_files:
            f.write(f"file '{os.path.basename(tf)}'\n")

    output_path = os.path.join(output_dir, f'{task_id}_output.mp3')

    subprocess.run([
        'ffmpeg', '-f', 'concat', '-safe', '0',
        '-i', list_path,
        '-c', 'copy',
        output_path,
        '-y'
    ], capture_output=True, cwd=output_dir)

    os.remove(list_path)
    for tf in temp_files:
        if os.path.exists(tf):
            os.remove(tf)

    tasks[task_id]['progress'] = 100
    tasks[task_id]['status'] = 'completed'
    tasks[task_id]['output'] = output_path

    if os.path.exists(filepath):
        os.remove(filepath)


def process_text_file(task_id, filepath, output_dir, tasks):
    try:
        asyncio.run(_process(task_id, filepath, output_dir, tasks))
    except Exception as e:
        tasks[task_id]['status'] = 'error'
        tasks[task_id]['error'] = str(e)
