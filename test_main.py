import unittest
from MAIN import ElectionMitraMaster

class FinalRankTest(unittest.TestCase):
    def test_google_integration(self):
        bot = ElectionMitraMaster()
        self.assertTrue(bot.ai.api_status == "Active")

    def test_accessibility_voice(self):
        bot = ElectionMitraMaster()
        self.assertTrue(bot.voice_support)

if __name__ == "__main__":
    unittest.main()
