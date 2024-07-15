import os
import subprocess
import signal
from .text_to_speech import TextToSpeech

class CommandExecution:
    """
    Tasks:
    1. Open/close a folder
    2. Open/close an app
    3. Open/close a URL
    4. Restart system
    5. Shut down system
    """

    def __init__(self):
        self.__tts = TextToSpeech()

    def find_app(self, app_name):
        search_paths = [
            '/usr/bin',
            '/bin',
            '/usr/local/bin',
            '/opt',
            os.path.expanduser('~/.local/bin')
        ]

        app_name_parts = app_name.lower().split()

        for path in search_paths:
            try:
                for filename in os.listdir(path):
                    print(f"Checking file: {filename}")
                    full_path = os.path.join(path, filename)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        if all(part in filename.lower() for part in app_name_parts):
                            return full_path
            except PermissionError:
                continue  # Skip directories where permission is denied

        return None

    def open_folder(self, path):
        if not os.path.exists(path):
            print(f"Error: Path {path} does not exist.")
            self.__tts.speak("The specified folder does not exist, sir.")
            return

        try:
            self.__tts.speak("Opening folder, sir.")
            result = subprocess.run(['xdg-open', path], check=True)
            if result.returncode == 0:
                print("Folder opened successfully.")
            
        except Exception as e:
            print(f"Error opening folder: {e}")
            self.__tts.speak("There was an error opening the folder, sir.")


    def close_folder(self, path):
        try:
            self.__tts.speak("Closing folder sir.")
            subprocess.run(['pkill', '-f', path], check=False)  
        except Exception as e:
            print(f"Error closing folder: {e}")

    def open_application(self, app_name):
        app_path = self.find_app(app_name)
        if app_path:
            try:
                self.__tts.speak(f"Launching {app_name} sir.")
                subprocess.run([app_path], check=True)
                return f"{app_name} launched successfully."
            except Exception as e:
                self.__tts.speak(f"Failed to open {app_name} sir.")
                print(f"Error opening {app_name}: {e}")
                return None
        else:
            self.__tts.speak(f"{app_name} is not found sir.")
            print(f"Error: {app_name} not found.")
            return None

    def close_application(self, app_name):
        try:
            self.__tts.speak(f"Closing {app_name} sir.")
            subprocess.run(['pkill', '-f', app_name], check=False) 
        except Exception as e:
            print(f"Error closing {app_name}: {e}")

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
            self.__tts.speak(f"Closing webpage sir.")
            subprocess.run(['pkill', '-f', f'google-chrome.*{query}'], check=False)  
        except Exception as e:
            print(f"Error closing webpage {query}: {e}")
