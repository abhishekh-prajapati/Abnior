# ABNIOR - Personalized AI Assistant

ABNIOR is a voice and gesture-driven AI assistant for Windows, built on Gemini.

## Features
- **Activation Sound**: "Abnior activated" on startup.
- **Voice Control**: Speak naturally; ABNIOR listens and responds in multiple languages.
- **Hand Gestures**: Confirm actions with hand signals (e.g., Thumb Up).
- **System Automation**: Open apps, search the web, send WhatsApp/Email messages.
- **Floating UI**: A sleek, sound-reactive design at the top center of your screen.

## Setup
1.  **Dependencies**: Install Python 3.10+ and run:
    ```bash
    pip install -r requirements.txt
    ```
2.  **API Keys**: Rename `.env` to `.env` (already done) and add your `GEMINI_API_KEY`.
3.  **Startup**: Run `.\setup_startup.ps1` in PowerShell to make ABNIOR launch automatically when you open your laptop.
4.  **Run**: Simply execute `python main.py`.

## Built With
- **AI**: Google Gemini API
- **Vision**: MediaPipe & OpenCV
- **Voice**: SpeechRecognition & pyttsx3
- **Automation**: pywhatkit & pyautogui
- **UI**: PyQt6
