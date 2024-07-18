import os


class CommandProcessor:
    """
    What this interface does:
    - If "open folder foo", it looks up foo from the path_mappings dictionary
    - Extracts app name and webpage name then uses that to open the app/page
    - Works hand in hand with the CommandExecution class
    """

    def __init__(self, cmd_executor):
        self.cmd_executor = cmd_executor
        self.path_mapping = {
            "desktop": os.path.expanduser("~/Desktop"),
            "documents": os.path.expanduser("~/Documents"),
            "downloads": os.path.expanduser("~/Downloads"),
            "pictures": os.path.expanduser("~/Pictures"),
            "music": os.path.expanduser("~/Music"),
            "videos": os.path.expanduser("~/Videos"),
            "usr_bin": '/usr/bin',
            "bin": '/bin',
            "usr_local_bin": '/usr/local/bin',
            "opt": '/opt',
            "local_bin": os.path.expanduser('~/.local/bin')
        }

    def parse_command(self, command):
        command = command.lower()
        action = {'type': None, 'parameters': {}}

        print(f"Parsing command: {command}")

        if "open folder" in command:
            action['type'] = 'open_folder'
            action['parameters']['path'] = self.extract_path(command)
        
        elif any(keyword in command for keyword in ["thank you", "never mind", "not now", "close self"]):
            action['type'] = 'close_jarvis'
            
        elif any(keyword in command for keyword in ["launch application", "start application"]):
            action['type'] = 'launch_application'
            action['parameters']['app_name'] = self.extract_app_name(command)

        elif any(keyword in command for keyword in ["close folder", "hide folder"]):
            action['type'] = 'close_folder'
            action['parameters']['path'] = self.extract_path(command)

        elif any(keyword in command for keyword in ["close application", "exit application"]):
            action['type'] = 'close_application'
            action['parameters']['app_name'] = self.extract_app_name(command)

        elif "shut down computer" in command:
            action['type'] = 'shut_down'

        elif "restart computer" in command:
            action['type'] = 'restart'

        elif "find webpage" in command:
            action['type'] = 'find_webpage'
            action['parameters']['query'] = self.extract_query(command)

        print(f"Action parsed: {action}")
        return action

    def do_this(self, command):
        print(f"Executing command: {command}")
        action = self.parse_command(command)
        print(f"Action to be performed: {action}")

        
        if action['type'] == 'open_folder':
            response = self.cmd_executor.open_folder(
                action['parameters']['path'])
            print(f"Response from open_folder: {response}")
            return response if response else "Failed to open folder."

        elif action['type'] == 'launch_application':
            response = self.cmd_executor.launch_application(
                action['parameters']['app_name'])
            print(f"Response from launch_application: {response}")
            return response if response else "Failed to open application."

        elif action['type'] == 'shut_down':
            self.cmd_executor.shut_down()
            print("Shutting down the system.")
            return "Shutting down the system."

        elif action['type'] == 'restart':
            self.cmd_executor.restart()
            print("Restarting the system.")
            return "Restarting the system."

        elif action['type'] == 'find_webpage':
            self.cmd_executor.find_webpage(action['parameters']['query'])
            print("Opening the webpage.")
            return "Opening the webpage."
        
        elif action['type'] == 'close_jarvis':
            return "Anytime sir."

        else:
            print(f"Unknown command: {command}")
            return "Sorry, I couldn't perform the action, sir."

    def extract_path(self, command):
        print(f"Extracting path from command: {command}")
        words = command.split()

        if "open folder" in command:
            # Extract everything after "open folder"
            folder_name = " ".join(words[2:]).strip()
            print(f"Extracted folder name: {folder_name}")

            for keyword, base_path in self.path_mapping.items():
                full_path = os.path.join(base_path, folder_name)
                if os.path.exists(full_path):
                    print(f"Found folder: {full_path}")
                    return full_path

            print("Folder does not exist in any mapped paths.")
            return None

        print("No valid command for path extraction.")
        return None

    def extract_app_name(self, command):
        print(f"Extracting app name from command: {command}")

        # Split the command into words
        words = command.split()

        if any(keyword in command for keyword in ["launch application", "start application", "close application", "exit application"]):

            keywords = ["launch application", "start application"]
            for keyword in keywords:
                if keyword in command:
                    app_words = command.split(keyword)[1].strip().split()
                    break

            print(f"Extracted app words: {app_words}")

            for path in self.path_mapping.values():
                if os.path.exists(path):
                    for filename in os.listdir(path):
                        full_path = os.path.join(path, filename)
                        if os.access(full_path, os.X_OK) and any(word.lower() in filename.lower() for word in app_words):
                            print(f"Found application: {full_path}")
                            return full_path

            print("Application does not exist in any mapped paths.")
            return None

        print("No valid command for app name extraction.")
        return None

    def extract_query(self, command):
        if "find webpage" in command:
            query = command.split("find webpage")[-1].strip()
            print(f"Extracted query: {query}")
            return query
        print("No query found.")
        return ""
