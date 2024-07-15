import os

class CommandProcessor:
    def __init__(self, cmd_executor):
        self.cmd_executor = cmd_executor
        self.path_mapping = {
            "desktop": os.path.expanduser("~/Desktop"),
            "documents": os.path.expanduser("~/Documents"),
            "downloads": os.path.expanduser("~/Downloads"),
            "pictures": os.path.expanduser("~/Pictures"),
            "music": os.path.expanduser("~/Music"),
            "videos": os.path.expanduser("~/Videos"),
        }

    def parse_command(self, command):
        command = command.lower()
        action = {'type': None, 'parameters': {}}

        print(f"Parsing command: {command}")

        if "open folder" in command:
            action['type'] = 'open_folder'
            action['parameters']['path'] = self.extract_path(command)

        elif any(keyword in command for keyword in ["launch", "start"]):
            action['type'] = 'open_application'
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
            response = self.cmd_executor.open_folder(action['parameters']['path'])
            print(f"Response from open_folder: {response}")
            return response if response else "Failed to open folder."

        elif action['type'] == 'open_application':
            response = self.cmd_executor.open_application(action['parameters']['app_name'])
            print(f"Response from open_application: {response}")
            return response if response else "Failed to open application."

        elif action['type'] == 'close_folder':
            response = self.cmd_executor.close_folder(action['parameters']['path'])
            print(f"Response from close_folder: {response}")
            return response if response else "Failed to close folder."

        elif action['type'] == 'close_application':
            response = self.cmd_executor.close_application(action['parameters']['app_name'])
            print(f"Response from close_application: {response}")
            return response if response else "Failed to close application."

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

        else:
            print(f"Unknown command: {command}")
            return "Sorry, I couldn't perform the action, sir."

    def extract_path(self, command):
        print(f"Extracting path from command: {command}")
        words = command.split()
        
        if "open folder" in command:
            # Extract folder name
            folder_name = " ".join(words[2:]).strip()  # Extract everything after "open folder"
            print(f"Extracted folder name: {folder_name}")

            # Check each path in path_mapping for the folder
            for keyword, base_path in self.path_mapping.items():
                # Construct the full path
                full_path = os.path.join(base_path, folder_name)

                if os.path.exists(full_path):
                    print(f"Found folder: {full_path}")
                    return full_path

            print("Folder does not exist in any mapped paths.")
            return None
        
        print("No valid command for path extraction.")
        return None
    
    def extract_app_name(self, command):
        for keyword in ["launch app", "exit app"]:
            if keyword in command:
                app_name = command.split(keyword)[-1].strip()
                print(f"Extracted app name: {app_name}")
                return app_name
        print("No app name found.")
        return ""

    def extract_query(self, command):
        if "find webpage" in command:
            query = command.split("find webpage")[-1].strip()
            print(f"Extracted query: {query}")
            return query
        print("No query found.")
        return ""
