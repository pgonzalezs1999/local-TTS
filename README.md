# 📢 Text to Speech TTS

Convert `.txt` files to speech using Microsoft **Edge-TTS**. A simple and elegant web interface to generate high-quality MP3 audio with neural voices in Spanish.

![Status](https://img.shields.io/badge/status-working-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/flask-3.0+-lightgrey)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## ✨ Features

- **Drag & drop** — Drag your `.txt` file and drop it onto the interface
- **Neural voices** — Uses Edge-TTS with realistic Spanish voices
- **No text limits** — Automatically splits long texts and concatenates the audio chunks
- **Direct download** — The MP3 is named after your original file (e.g. `speech.txt` → `speech.mp3`)
- **Clean UI** — Minimalist, responsive design

---

## 📋 Prerequisites

| Tool | Version | Why |
|---|---|---|
| [Python](https://www.python.org/downloads/) | 3.8 or higher | Core language |
| [pip](https://pip.pypa.io/en/stable/) | — | Python package manager |
| [ffmpeg](https://ffmpeg.org/download.html) | Any | Concatenates audio chunks into a single MP3 |

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
</details>

<details>
<summary><b>Linux (Ubuntu/Debian)</b></summary>

```bash
sudo apt update && sudo apt install ffmpeg -y
```

Other distributions use their respective package managers (`pacman`, `dnf`, etc.).
</details>

<details>
<summary><b>macOS</b></summary>

```bash
brew install ffmpeg
```

If you don't have Homebrew, install it from [brew.sh](https://brew.sh).
</details>

---

## 🚀 Installation

### 1. Clone or download the repository

```bash
git clone https://github.com/yourusername/localTTS.git
cd localTTS
```

### 2. Create a virtual environment (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the voice (optional)

Copy `.env.example` to `.env` and edit it if you want to change the voice:

```bash
cp .env.example .env
```

The default voice is `es-ES-ElviraNeural`. You can change it to any Edge-TTS voice — check the [full list](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts).

---

## ▶️ Running

### Option 1: Double-click (Windows)

Just double-click **`iniciar.bat`**. It will start the server (minimized) and open your browser at `http://localhost:5000`.

### Option 2: Terminal (all platforms)

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

### Option 3: Script for Linux / macOS

```bash
chmod +x iniciar.sh
./iniciar.sh
```

---

## 🎯 How to use

1. Drag a `.txt` file onto the dashed area or click to select one
2. Click **Generar Audio**
3. Wait for the progress bar to reach 100%
4. Click **Descargar MP3**

The downloaded file will have the same name as your `.txt` file (e.g. `speech.txt` → `speech.mp3`).

---

## 🗂️ Project structure

```
localTTS/
├── app.py              # Flask server
├── tts_engine.py       # Text-to-speech engine
├── requirements.txt    # Python dependencies
├── .env.example        # Sample configuration
├── iniciar.bat         # Quick start for Windows
├── iniciar.sh          # Quick start for Linux/Mac
├── templates/
│   └── index.html      # Web interface
├── uploads/            # Uploaded files (temporary)
└── outputs/            # Generated audio files
```

---

## 🛠️ Tech stack

- **Backend:** Python, Flask
- **TTS:** Edge-TTS (Microsoft)
- **Audio:** ffmpeg
- **Frontend:** HTML, CSS, Vanilla JavaScript

---

## 📄 License

MIT — Use, share, modify, and learn freely.

---

<p align="center">Built by <a href="https://github.com/pgonzalezs1999">pgonzalezs1999</a></p>
