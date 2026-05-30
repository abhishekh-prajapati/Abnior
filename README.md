# ABNIOR – AI Desktop Assistant for Windows

ABNIOR is an intelligent desktop assistant built for Windows that combines voice interaction, computer vision, gesture recognition, and automation into a unified AI-powered experience.

Unlike traditional assistants that rely only on voice commands, ABNIOR can understand spoken instructions, interpret hand gestures for confirmation, automate everyday tasks, and provide a seamless floating interface that stays accessible while you work.

---

## 🚀 Key Features

### 🎙️ Voice-First Interaction

* Natural voice conversations powered by Google Gemini.
* Supports multiple languages and accents.
* Wake-up and activation audio feedback.
* Real-time speech recognition and response generation.

### ✋ Gesture-Based Confirmation

* Uses computer vision to detect hand gestures.
* Perform actions securely through gesture confirmation.
* Supports gestures such as:

  * 👍 Thumb Up → Confirm Action
  * ✋ Open Palm → Cancel/Reject Action
* Reduces accidental execution of sensitive tasks.

### ⚡ System Automation

ABNIOR can automate common desktop activities, including:

* Launching applications
* Opening websites
* Web searching
* Sending WhatsApp messages
* Sending emails
* Managing productivity workflows
* Executing custom commands

### 🌐 Intelligent AI Responses

* Powered by Google Gemini.
* Context-aware conversations.
* Information retrieval and assistance.
* Task planning and recommendations.

### 🎨 Floating Desktop Interface

* Modern floating assistant window.
* Sound-reactive visual effects.
* Lightweight and non-intrusive design.
* Positioned at the top-center of the screen for quick access.

### 🔊 Audio Feedback System

* Activation sound on startup.
* Voice responses for commands.
* Interactive conversational experience.

---

## 🏗️ Technology Stack

### Artificial Intelligence

* Google Gemini API

### Computer Vision

* OpenCV
* MediaPipe

### Speech Processing

* SpeechRecognition
* pyttsx3

### Desktop Automation

* PyAutoGUI
* PyWhatKit

### User Interface

* PyQt6

### Programming Language

* Python 3.10+

---

## 📂 Project Architecture

```text
ABNIOR/
│
├── main.py                 # Main application entry point
├── assistant/              # Core AI assistant logic
├── automation/             # Desktop automation modules
├── vision/                 # Gesture recognition system
├── speech/                 # Speech recognition & TTS
├── ui/                     # Floating desktop interface
├── assets/                 # Sounds, icons and resources
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── setup_startup.ps1       # Startup configuration
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd ABNIOR
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create or update the `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

### 4. Enable Startup Launch (Optional)

Run PowerShell as Administrator:

```powershell
.\setup_startup.ps1
```

This allows ABNIOR to automatically start whenever Windows launches.

### 5. Launch ABNIOR

```bash
python main.py
```

---

## 💡 Example Commands

### Voice Commands

```text
Open Chrome
```

```text
Search AWS Summit Mumbai
```

```text
Send a WhatsApp message to John
```

```text
Open Visual Studio Code
```

```text
What are today's technology news updates?
```

---

## 🔒 Security Considerations

* Sensitive actions can require gesture confirmation.
* API keys are stored using environment variables.
* User credentials are never hardcoded into the application.

---

## 🎯 Future Roadmap

* Face recognition support
* Custom wake words
* Local LLM integration
* Smart home device control
* Advanced workflow automation
* Plugin ecosystem
* Cross-platform support (Linux & macOS)
* Calendar and productivity integrations

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Abhishekh**.

ABNIOR aims to create a next-generation desktop assistant that combines AI intelligence, voice interaction, computer vision, and automation into a single seamless experience.
