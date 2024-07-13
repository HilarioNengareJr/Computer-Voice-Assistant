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
        pass

    def do_this(self, command):

        action = self.parse_command(command)
        if action['type'] == 'open_folder':
            self.file_manager.open_folder(action['path'])
        elif action['type'] == 'play_music':
            self.music_player.play_music(action['path'])
