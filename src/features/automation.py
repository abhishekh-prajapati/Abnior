import os
import subprocess
import webbrowser
import pyautogui
import pywhatkit as kit
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

class SystemControl:
    def open_app(self, app_name):
        try:
            print(f"Opening {app_name}...")
            # Simple approach: use 'start' command in Windows
            subprocess.run(f"start {app_name}", shell=True)
            return True
        except Exception as e:
            print(f"Error opening app: {e}")
            return False

    def close_app(self, app_name):
        try:
            print(f"Closing {app_name}...")
            # Use 'taskkill' command in Windows
            subprocess.run(f"taskkill /f /im {app_name}.exe", shell=True)
            return True
        except Exception as e:
            print(f"Error closing app: {e}")
            return False

    def search_web(self, query):
        print(f"Searching for {query}...")
        webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")

class Automation:
    def __init__(self):
        self.email = os.getenv("EMAIL_ADDRESS")
        self.password = os.getenv("EMAIL_PASSWORD")

    def send_whatsapp(self, number, message):
        try:
            print(f"Sending WhatsApp message to {number}...")
            # Kit sends it instantly at current time
            kit.sendwhatmsg_instantly(number, message) 
            return True
        except Exception as e:
            print(f"WhatsApp Error: {e}")
            return False

    def send_email(self, destination, subject, body):
        try:
            print(f"Sending Email to {destination}...")
            msg = EmailMessage()
            msg.set_content(body)
            msg['Subject'] = subject
            msg['From'] = self.email
            msg['To'] = destination

            # Standard Gmail setup
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(self.email, self.password)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"Email Error: {e}")
            return False

if __name__ == "__main__":
    pass
