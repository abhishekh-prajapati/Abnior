import pyttsx3
import threading

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id) # Set to default voice
        self.engine.setProperty('rate', 150) # Set speed
        self.engine.setProperty('volume', 1.0) # Set volume

    def speak(self, text):
        def _speak():
            print(f"ABNIOR says: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        
        # Use a thread so that speaking doesn't block other tasks
        threading.Thread(target=_speak).start()

    def set_voice(self, index):
        if index < len(self.voices):
          self.engine.setProperty('voice', self.voices[index].id)

if __name__ == "__main__":
    tts = TTS()
    tts.speak("Abnior activated")
