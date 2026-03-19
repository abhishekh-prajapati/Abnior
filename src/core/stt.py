import speech_recognition as sr
import sounddevice as sd
import numpy as np
import io
from scipy.io.wavfile import write

class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.sample_rate = 16000 # Standard for speech recognition

    def record_audio(self, duration=5):
        print("Recording...")
        # Record audio using sounddevice
        audio_data = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='int16')
        sd.wait() # Wait for recording to finish
        print("Recording finished.")
        return audio_data

    def listen(self, timeout=5):
        try:
            audio_np = self.record_audio(duration=timeout)
            
            # Convert numpy array to WAV bytes in memory
            byte_io = io.BytesIO()
            write(byte_io, self.sample_rate, audio_np)
            byte_io.seek(0)
            
            # Use speech_recognition to process the WAV data
            with sr.AudioFile(byte_io) as source:
                audio = self.recognizer.record(source)
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
                return text
        except (sr.UnknownValueError, sr.RequestError):
            return None
        except Exception as e:
            print(f"Error in STT: {e}")
            return None

    def wait_for_wake_word(self, wake_word="abnior"):
        print(f"Waiting for wake word '{wake_word}'...")
        while True:
            try:
                # Continuously record small chunks and check
                audio_np = self.record_audio(duration=2)
                byte_io = io.BytesIO()
                write(byte_io, self.sample_rate, audio_np)
                byte_io.seek(0)
                
                with sr.AudioFile(byte_io) as source:
                    audio = self.recognizer.record(source)
                    text = self.recognizer.recognize_google(audio).lower()
                    if wake_word in text:
                        print("Wake word detected!")
                        return True
            except (sr.UnknownValueError, sr.RequestError):
                continue
            except Exception as e:
                print(f"Error in wake word detection: {e}")
                break
        return False

if __name__ == "__main__":
    stt = STT()
    print(stt.listen())
