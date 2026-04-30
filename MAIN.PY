import time
import sys

class GlobalElectionBot:
    def __init__(self):
        # Multi-language database
        self.content = {
            "en": {
                "welcome": "\n--- ELECTION INFORMATION SYSTEM ---",
                "menu": "\n1. View Timeline\n2. Step Details\n3. Exit",
                "prompt": "Select an option: ",
                "steps": {
                    "1": "Voter Registration: Verify your name in the roll.",
                    "2": "Nomination: Candidates file official papers.",
                    "3": "Campaigning: Parties share their manifestos.",
                    "4": "Voting: Cast your ballot at the booth.",
                    "5": "Results: Final counting and declaration."
                }
            },
            "hi": {
                "welcome": "\n--- चुनाव सूचना प्रणाली ---",
                "menu": "\n1. टाइमलाइन देखें\n2. स्टेप की जानकारी\n3. बाहर निकलें",
                "prompt": "विकल्प चुनें: ",
                "steps": {
                    "1": "वोटर रजिस्ट्रेशन: वोटर लिस्ट में अपना नाम चेक करें।",
                    "2": "नामांकन: उम्मीदवार अपना पर्चा भरते हैं।",
                    "3": "चुनाव प्रचार: पार्टियां अपना मेनिफेस्टो बताती हैं।",
                    "4": "मतदान: पोलिंग बूथ पर जाकर वोट दें।",
                    "5": "परिणाम: वोटों की गिनती और नतीजों की घोषणा।"
                }
            }
        }
        self.lang = "en" # Default language

    def select_language(self):
        print("Choose your language / अपनी भाषा चुनें:")
        print("1. English\n2. Hindi")
        choice = input("Choice (1/2): ").strip()
        self.lang = "hi" if choice == "2" else "en"

    def run(self):
        self.select_language()
        lang_pack = self.content[self.lang]
        print(lang_pack["welcome"])

        while True:
            print(lang_pack["menu"])
            choice = input(lang_pack["prompt"]).strip()

            if choice == "1":
                print("\n--- TIMELINE ---")
                for k, v in lang_pack["steps"].items():
                    print(f"Step {k}: {v.split(':')[0]}")
                    time.sleep(0.3)
            elif choice == "2":
                step_no = input("Enter Step (1-5): ").strip()
                detail = lang_pack["steps"].get(step_no, "Invalid")
                print(f"\nInfo: {detail}")
            elif choice == "3":
                print("Exiting...")
                break

if __name__ == "__main__":
    bot = GlobalElectionBot()
    bot.run()