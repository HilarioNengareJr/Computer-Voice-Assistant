import os
import subprocess
from .text_to_speech import TextToSpeech

class CommandExecution:

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
                    full_path = os.path.join(path, filename)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        # Check if any part of the app_name matches the filename
                        if all(part in filename.lower() for part in app_name_parts):
                            
                            return full_path
            except PermissionError:
                # Skip directories where permission is denied
                continue

        return None

    def open_folder(self, path):
        if not os.path.exists(path):
            self.__tts.speak(f"We have an Error sir which says Path {path} does not exist.")
            print(f"Error: Path {path} does not exist.")
            return

        try:
            self.__tts.speak(f"Opening folder sir")
            subprocess.Popen(['xdg-open', path])
        except Exception as e:
            self.__tts.speak(f"could not open folder sir")
            print(f"Error opening folder {path}: {e}")

    def open_application(self, app_name):
        app_path = self.find_app(app_name)
        if app_path:
            try:
                self.__tts.speak(f"Launching application at {app_name} sir.")
                subprocess.run([app_path], check=True)  
                return "Application launched successfully."  
            except Exception as e:
                self.__tts.speak(f"Failed to open application sir.")
                print(f"Error opening application {app_name}: {e}")
                return None 
        else:
            self.__tts.speak(f"Application {app_name} is not found sir.")
            print(f"Error: Application {app_name} not found.")
            return None 


    def shut_down(self):
        try:
            self.__tts.speak(f"Shutting down the system sir")
            subprocess.run(["shutdown", "now"])
        except Exception as e:
            print(f"Error shutting down the computer: {e}")

    def restart(self):
        try:
            self.__tts.speak(f"Restarting the system sir")
            subprocess.run(["reboot"])
        except Exception as e:
            print(f"Error restarting the computer: {e}")

    def find_webpage(self, query):
        url = f"https://www.google.com/search?q={query}"
        try:
            self.__tts.speak(f"Opening {url} sir")
            subprocess.run(["google-chrome", url])
        except Exception as e:
            print(f"Error opening webpage {query}: {e}")
