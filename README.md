# 📢 Text to Speech TTS

Convert `.txt` files to speech using Microsoft **Edge-TTS**. A simple and elegant web interface to generate high-quality MP3 audio with neural voices in Spanish.

---

## 📋 Prerequisites

| Tool | Version |
|---|---|---|
| [Python](https://www.python.org/downloads/) | 3.8 or higher |
| [pip](https://pip.pypa.io/en/stable/) | — |
| [ffmpeg](https://ffmpeg.org/download.html) | Any |

### Installing ffmpeg

<details>
<summary><b>Windows</b></summary>

1. Download the binary from [ffmpeg.org](https://ffmpeg.org/download.html#build-windows)
2. Extract it to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to your system PATH:
   - Open "Edit environment variables"
   - Under "System variables", select `Path` → "Edit" → "New"
   - Paste `C:\ffmpeg\bin`
4. Verify with: `ffmpeg -version`
5. Install dependencies:
```bash
pip install -r requirements.txt
```
</details>

<details>
<summary><b>Linux</b></summary>

1. Set up proyect
```bash
sudo apt update && sudo apt install ffmpeg -y
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
</details>

<details>
<summary><b>macOS</b></summary>

1. Set up proyect
```bash
brew install ffmpeg
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
</details>

---

## ▶️ Running

### Option 1: Double-click (Windows)

Just double-click **`start.bat`**. It will start the server (minimized) and open your browser at `http://localhost:5000`.

### Option 2: Terminal (all platforms)

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

### Option 3: Script for Linux / macOS

```bash
chmod +x start.sh
./start.sh
```

---

## 🎯 How to use

1. Drag a `.txt` file onto the dashed area or click to select one
2. Click **Generate Audio**
3. Wait for the progress bar to reach 100%
4. Click **Download MP3**