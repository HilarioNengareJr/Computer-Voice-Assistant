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
            if all(keyword not in command.lower() for keyword in ["thank you", "never mind", "not now", "close self"]):
                self.speaker.speak(f"Processing command: {command}")
                print(f"Recognized command: {command}")
                response = self.command_processor.do_this(command)
            else:
                self.speaker.speak("Anytime sir.")
                return
            
            if response:
                self.speaker.speak(response)
                print(response)
            elif response is None:
                self.speaker.speak("Sorry, I couldn't perform the action sir.")
                print("Sorry, I couldn't perform the action sir.")
            else:
                self.speaker.speak("Command processed successfully.")
                print("Command processed successfully.")

            if command.lower() == "jarvis exit":
                self.speaker.speak("Exiting, sir.")
                print("Exiting...")
                sys.exit(0)
        else:
            self.speaker.speak("I didn't catch that. Could you please repeat sir?")
            print("I didn't catch that. Could you please repeat?")
