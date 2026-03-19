import sys
import threading
import time
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

# Set DPI awareness for high-resolution displays
if os.name == 'nt':
    from ctypes import windll
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

from src.core.brain import Brain
from src.core.stt import STT
from src.core.tts import TTS
from src.features.automation import SystemControl, Automation
from src.features.vision import Vision
from src.ui.overlay import AIDesign

class AbniorApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = AIDesign()
        self.brain = Brain()
        self.stt = STT()
        self.tts = TTS()
        self.system = SystemControl()
        self.automation = Automation()
        
        self.is_running = True
        self.last_gesture_time = 0.0
        
        # Fallback for Vision (which needs .task model files)
        self.vision = None
        try:
            self.vision = Vision()
            print("Vision system activated (Hand Gestures enabled)")
        except Exception as e:
            print(f"Vision system fallback: Hand gestures disabled (Error: {e})")
        
        # Start AI logic in a background thread
        self.ai_thread = threading.Thread(target=self.ai_loop)
        self.ai_thread.daemon = True
        self.ai_thread.start()

    def ai_loop(self):
        # Activation sound
        self.tts.speak("Abnior activated")
        
        while self.is_running:
            # First, wait for the wake word "Abnior"
            self.ui.set_status("IDLE")
            if self.stt.wait_for_wake_word():
                # Wake word detected
                self.ui.set_status("LISTENING")
                self.tts.speak("Yes?") # Auditory confirmation
                
                # Check for hand gestures only if vision system initialized correctly
                if self.vision:
                    gesture = self.vision.detect_gesture()
                    if gesture == "THUMB_UP":
                        self.handle_gesture_trigger()
                
                # Listen for the actual command
                text = self.stt.listen(timeout=5)
                if text:
                    self.ui.set_status("SPEAKING")
                    response = self.brain.process_command(text)
                    self.tts.speak(response)
                    self.execute_commands(response)
                
                self.ui.set_status("IDLE")
            
            time.sleep(0.1)

    def handle_gesture_trigger(self):
        now = time.time()
        if now - self.last_gesture_time > 2: # Limit trigger frequency
            self.last_gesture_time = now
            print("Gesture trigger: Confirming action...")
            self.tts.speak("Confirmed by gesture")

    def execute_commands(self, text):
        # Very simple keyword-based execution for now
        # Ideally, Brain should output structured data to trigger functions
        lower_text = text.lower()
        if "open browser" in lower_text:
            self.system.open_app("chrome")
        elif "search" in lower_text:
            # Simple heuristic
            query = lower_text.split("search")[-1].strip()
            self.system.search_web(query)
        # ... Add more command mappings ...

    def run(self):
        self.ui.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = AbniorApp()
    app.run()
