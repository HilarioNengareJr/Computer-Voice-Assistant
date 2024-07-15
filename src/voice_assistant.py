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
        
    def listen_and_respond(self):
        command = self.recognizer.recognize_speech()
        
        if command:
            self.speaker.speak(f"Initializing command: {command}")
            print(f"Recognized command: {command}")
            response = self.command_processor.do_this(command)
            if response:
                self.speaker.speak(response)
                print(response)
            else:
                self.speaker.speak("Sorry, I couldn't perform the action sir.")
                print("Sorry, I couldn't perform the action sir.")
        else:
            self.speaker.speak("I didn't catch that. Could you please repeat sir?")
            print("I didn't catch that. Could you please repeat?")
