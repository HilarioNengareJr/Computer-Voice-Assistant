import os, subprocess
from .command_processor import CommandProcessor
from .text_to_speech import TextToSpeech

class CommandExecution(CommandProcessor):
    """
    Tasks:
    1. Open/close a folder
    2. Open/close an app
    3. Open/close a URL
    4. Restart system
    5. Shut down system
    """

    def __init__(self):
        super().__init__(self)  
        self.__tts = TextToSpeech()

    def open_folder(self, path):
        if not os.path.exists(path):
            print(f"Error: Path {path} does not exist.")
            self.__tts.speak("The specified folder does not exist, sir.")
            return "Folder does not exist."

        try:
            subprocess.run(['xdg-open', path], check=True)
            self.__tts.speak("Opening folder, sir.")
            return "Folder opened successfully."
        except Exception as e:
            print(f"Error opening folder: {e}")
            self.__tts.speak("There was an error opening the folder, sir.")
            return "Failed to open folder."

    def close_folder(self, path):
        try:
            self.__tts.speak("Closing folder sir.")
            subprocess.run(['pkill', '-f', path], check=False)
        except Exception as e:
            print(f"Error closing folder: {e}")

    def launch_application(self, app_path):
        if app_path:
            try:
                self.__tts.speak("Launching application sir.")
                subprocess.run([app_path], check=True)
                return "Application launched successfully."
            except Exception as e:
                self.__tts.speak("Failed to open application sir.")
                print(f"Error opening application: {e}")
                return None
        else:
            self.__tts.speak("Application is not found sir.")
            print("Error: Application not found.")
            return None

    def close_application(self, app_path):
        try:
            self.__tts.speak("Closing application sir.")
            subprocess.run(['pkill', '-f', app_path], check=False)
        except Exception as e:
            print(f"Error closing application: {e}")

    def shut_down(self):
        try:
            self.__tts.speak("Shutting down the system sir.")
            subprocess.run(["shutdown", "now"], check=True)
            return "System shutting down."
        except Exception as e:
            return f"Error shutting down the computer: {e}"

    def restart(self):
        try:
            self.__tts.speak("Restarting the system sir.")
            subprocess.run(["reboot"], check=True)
            return "Restarting ..."
        except Exception as e:
            return f"Error restarting the computer: {e}"

    def find_webpage(self, query):
        url = f"https://www.google.com/search?q={query}"
        try:
            self.__tts.speak(f"Opening {url} sir.")
            subprocess.run(["google-chrome", url], check=True)
            return "Opened URL."
        except Exception as e:
            return f"Error opening webpage {query}: {e}"

    def close_webpage(self, query):
        try:
            self.__tts.speak("Closing webpage sir.")
            subprocess.run(['pkill', '-f', query], check=False)
        except Exception as e:
            print(f"Error closing webpage: {e}")