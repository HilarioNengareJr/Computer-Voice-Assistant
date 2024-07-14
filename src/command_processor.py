class CommandProcessor:
    def __init__(self, cmd_executor):
        self.cmd_executor = cmd_executor

    def parse_command(self, command):
        command = command.lower()
        action = {'type': None, 'parameters': {}}

        if any(keyword in command for keyword in ["open folder", "show folder", "browse folder"]):
            action['type'] = 'open_folder'
            action['parameters']['path'] = self.extract_path(command)

        elif any(keyword in command for keyword in ["open", "launch", "start"]):
            action['type'] = 'open_application'
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
            self.cmd_executor.open_folder(action['parameters']['path'])
            return "Opened the folder."

        elif action['type'] == 'open_application':
            response = self.cmd_executor.open_application(action['parameters']['app_name'])
            return response if response else "Failed to open application."

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
            return "Sorry, I couldn't perform the action sir."
        
    def extract_path(self, command):
        if "folder" in command:
            return command.split("folder")[-1].strip()
        return ""

    def extract_app_name(self, command):
        for keyword in ["open", "launch", "start"]:
            if keyword in command:
                return command.split(keyword)[-1].strip()
        return ""

    def extract_query(self, command):
        return command.split("find webpage")[-1].strip()
