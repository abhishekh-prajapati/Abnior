import json
import os

class Memory:
    def __init__(self, filepath="p:\\Abnior\\memory.json"):
        self.filepath = filepath
        self.data = self.load()

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                return json.load(f)
        return {"mistakes": [], "user_preferences": {}}

    def learn_from_mistake(self, mistake, correction):
        self.data["mistakes"].append({"mistake": mistake, "correction": correction})
        self.save()

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_context(self):
        # Format mistakes for LLM inclusion
        if not self.data["mistakes"]:
            return ""
        
        mistake_str = "\n".join([f"Mistake: {m['mistake']} -> Correction: {m['correction']}" for m in self.data["mistakes"][-10:]])
        return f"\nRecent learning points:\n{mistake_str}"

if __name__ == "__main__":
    m = Memory()
    m.learn_from_mistake("Opened Chrome instead of Edge", "User prefers Edge")
    print(m.get_context())
