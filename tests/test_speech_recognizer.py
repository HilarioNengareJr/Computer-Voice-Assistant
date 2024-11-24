import unittest
from src.speech_recognizer import SpeechRecognizer

class TestSpeechRecognizer(unittest.TestCase):
    def setUp(self):
        self.recognizer = SpeechRecognizer()

    def test_recognize_speech(self):
        # Test the recognize_speech method
        recognized_text = self.recognizer.recognize_speech()
        # Add assertions here to check if the speech was recognized correctly

if __name__ == '__main__':
    unittest.main()
