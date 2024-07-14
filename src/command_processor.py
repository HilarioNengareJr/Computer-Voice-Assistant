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

        if any(keyword in command for keyword in ["open folder", "show folder", "browse folder"]):
            action['type'] = 'open_folder'
            action['parameters']['path'] = self.extract_path(command)

        elif any(keyword in command for keyword in ["launch", "start"]):
            action['type'] = 'open_application'
            action['parameters']['app_name'] = self.extract_app_name(command)

        # Add closing commands
        elif any(keyword in command for keyword in ["close folder", "hide folder"]):
            action['type'] = 'close_folder'
            action['parameters']['path'] = self.extract_path(command)

        elif any(keyword in command for keyword in ["close", "exit"]):
            action['type'] = 'close_application'
            action['parameters']['app_name'] = self.extract_app_name(command)

        elif "shut down computer" in command:
            action['type'] = 'shut_down'

        elif "restart computer" in command:
            action['type'] = 'restart'

        elif "find" in command and "webpage" in command:
            action['type'] = 'find_webpage'
            action['parameters']['query'] = self.extract_query(command)

        return action

    def do_this(self, command):
        action = self.parse_command(command)

        if action['type'] == 'open_folder':
            response = self.cmd_executor.open_folder(action['parameters']['path'])
            return response if response else "Failed to open folder."

        elif action['type'] == 'open_application':
            response = self.cmd_executor.open_application(action['parameters']['app_name'])
            return response if response else "Failed to open application."

        elif action['type'] == 'close_folder':
            response = self.cmd_executor.close_folder(action['parameters']['path'])
            return response if response else "Failed to close folder."

        elif action['type'] == 'close_application':
            response = self.cmd_executor.close_application(action['parameters']['app_name'])
            return response if response else "Failed to close application."

        elif action['type'] == 'shut_down':
            self.cmd_executor.shut_down()
            return "Shutting down the system."

        elif action['type'] == 'restart':
            self.cmd_executor.restart()
            return "Restarting the system."

        elif action['type'] == 'find_webpage':
            self.cmd_executor.find_webpage(action['parameters']['query'])
            return "Opening the webpage."

        else:
            print(f"Unknown command: {command}")
            return "Sorry, I couldn't perform the action, sir."

    def extract_path(self, command):
        for keyword, path in self.path_mapping.items():
            if keyword in command:
                folder_name = command.split(keyword)[-1].strip()
                full_path = os.path.join(path, folder_name)
                return full_path if os.path.exists(full_path) else None
        return None

    def extract_app_name(self, command):
        for keyword in ["launch", "start", "close", "exit"]:
            if keyword in command:
                return command.split(keyword)[-1].strip()
        return ""

    def extract_query(self, command):
        if "find webpage" in command:
            return command.split("find webpage")[-1].strip()
        return ""

