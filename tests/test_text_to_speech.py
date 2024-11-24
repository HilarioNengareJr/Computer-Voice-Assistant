import unittest
from src.text_to_speech import TextToSpeech

class TestTextToSpeech(unittest.TestCase):
    def setUp(self):
        self.speaker = TextToSpeech()

    def test_speak(self):
        # Test the speak method
        self.speaker.speak("Hello, world!")
        # Add assertions here to check if the text was spoken correctly

if __name__ == '__main__':
    unittest.main()
