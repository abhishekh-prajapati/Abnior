from google import genai
import os
from dotenv import load_dotenv
from src.core.memory import Memory

load_dotenv()

class Brain:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file")
        
        # New SDK syntax
        self.client = genai.Client(api_key=api_key)
        self.memory = Memory()
        self.model_name = 'gemini-1.5-pro' # Or gemini-1.5-flash
        
        # Initial context setup
        self.system_prompt = f"""
        You are ABNIOR, a powerful personal AI assistant. 
        You work on Windows and can control the laptop's features.
        Your personality: Efficient, proactive, and highly capable. 
        You respond with clarity.
        You support multilinguality.
        You can:
        - Open, close, create, edit, and delete files/apps.
        - Search real-time data.
        - Send WhatsApp messages and emails.
        - Learn from user feedback.
        
        Keep responses concise for voice output (under 20 words if possible).
        
        {self.memory.get_context()}
        """
        # Start a chat session or just send initial system instructions
        # The new SDK handles system instructions in generate_content or chat config
        self.chat = self.client.chats.create(
            model=self.model_name,
            config={'system_instruction': self.system_prompt}
        )

    def process_command(self, text):
        try:
            # Re-fetch context if memory has updated (not strictly needed every time but good for learning)
            context = self.memory.get_context()
            if context:
                text = f"[Context update: {context}]\n{text}"
            
            response = self.chat.send_message(text)
            return response.text
        except Exception as e:
            # Let's handle errors gracefully
            if "NOT_FOUND" in str(e) or "404" in str(e):
                return "Model error: The AI brain could not be initialized correctly. Please check model name."
            return f"Error: {str(e)}"

    def learn_from_feedback(self, text, correction):
        self.memory.learn_from_mistake(text, correction)
        self.chat.send_message(f"Update: I have learned from my feedback. {correction}. I will remember this.")

if __name__ == "__main__":
    b = Brain()
    print(b.process_command("Who are you?"))
