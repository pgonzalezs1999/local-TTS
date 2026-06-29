#!/bin/bash
echo "Iniciando servidor TTS..."
python app.py &
sleep 3
xdg-open http://localhost:5000 2>/dev/null || open http://localhost:5000 2>/dev/null || echo "Abre http://localhost:5000 en tu navegador"
echo "Servidor corriendo en http://localhost:5000"
echo "Presiona Ctrl+C para detenerlo"
wait
