class VoiceAssistant:
    """
    - Features of VA class-

    1. receive audio input
    2. translate audio input into text
    3. respond with requested output
    """

    def __init__(self, recognizer, speaker, command_processor):
        self.recognizer = recognizer
        self.speaker = speaker
        self.command_processor = command_processor
        
    def listen(self):
        command = self.recognizer.recognize_speech()
        self.command_processor.do_this(command)
        
    def respond(self, text):
        self.speaker.speak(text)
        
        
