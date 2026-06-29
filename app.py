import os
import json
import uuid
import threading
from flask import Flask, render_template, request, jsonify, send_file

from tts_engine import process_text_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['OUTPUT_FOLDER'] = os.path.join(os.path.dirname(__file__), 'outputs')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

tasks = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file was provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file was selected'}), 400

    task_id = str(uuid.uuid4())
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f'{task_id}.txt')
    original_name = os.path.splitext(file.filename)[0]
    file.save(filepath)

    tasks[task_id] = {'progress': 0, 'status': 'processing', 'output': None, 'error': None, 'original_name': original_name}

    thread = threading.Thread(
        target=process_text_file,
        args=(task_id, filepath, app.config['OUTPUT_FOLDER'], tasks)
    )
    thread.daemon = True
    thread.start()

    return jsonify({'task_id': task_id})

@app.route('/progress/<task_id>')
def get_progress(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({
        'progress': task['progress'],
        'status': task['status'],
        'error': task.get('error')
    })

@app.route('/download/<task_id>')
def download(task_id):
    task = tasks.get(task_id)
    if not task or task['status'] != 'completed':
        return jsonify({'error': 'File not available'}), 404
    download_name = f"{task.get('original_name', 'audio')}.mp3"
    return send_file(task['output'], as_attachment=True, download_name=download_name)

if __name__ == '__main__':
    app.run(debug=False, port=5000)
