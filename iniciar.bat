@echo off
title TTS Local - Servidor
echo Iniciando servidor TTS...
start /min "" python app.py
timeout /t 3 >nul
start "" http://localhost:5000
echo.
echo Servidor corriendo en http://localhost:5000
echo Para detenerlo, cierra la ventana "TTS Local - Servidor" minimizada.
pause
