class CommandProcessor:
    """
    -Features of Command Processor-

    1. take command input in the form of text
    2. execute the command 
    """

    def __init__(self, file_manager, music_player):

        self.file_manager = file_manager
        self.music_player = music_player

    def parse_command(self, command):
        command = command.lower()
        action = {'type': None, 'parameters': {}}

        if any(keyword in command for keyword in ["open folder", "show folder", "browse folder"]):
            action['type'] = 'open_folder'
            action['parameters']['path'] = self.extract_path(command)

        elif any(keyword in command for keyword in ["open", "launch", "start"]):
            action['type'] = 'open_application'
            action['parameters']['app_name'] = self.extract_app_name(command)

        elif any(keyword in command for keyword in ["play music", "start music", "play song"]):
            action['type'] = 'play_music'
            action['parameters']['file_path'] = self.extract_music_path(command)

        elif any(keyword in command for keyword in ["stop music", "pause music"]):
            action['type'] = 'stop_music'
            
        return action
            
            
    def do_this(self, command):

        action = self.parse_command(command)
        if action['type'] == 'open_folder':
            self.file_manager.open_folder(action['parameters']['path'])
        elif action['type'] == 'open_application':
            self.file_manager.open_application(action['parameters']['app_name'])
        elif action['type'] == 'play_music':
            self.music_player.play_music(action['parameters']['file_path'])
        elif action['type'] == 'stop_music':
            self.music_player.stop_music()

    def extract__path(self, command):
        return command.split("folder")[-1].strip()
    
    def extract_app_name(self, command):
        return command.split("open")[-1].strip()

    def extract_music_path(self, command):
        return command.split("music")[-1].strip()