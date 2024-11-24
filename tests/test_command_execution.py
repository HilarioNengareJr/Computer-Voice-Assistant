import unittest
from src.command_execution import CommandExecution

class TestCommandExecution(unittest.TestCase):
    def setUp(self):
        self.cmd_executor = CommandExecution()

    def test_open_folder(self):
        # Test the open_folder method
        self.cmd_executor.open_folder("/tmp")
        # Add assertions here to check if the folder was opened correctly

    def test_launch_application(self):
        # Test the launch_application method
        self.cmd_executor.launch_application("/usr/bin/gedit")
        # Add assertions here to check if the application was launched correctly

    def test_restart(self):
        # Test the restart method
        self.cmd_executor.restart()
        # Add assertions here to check if the system was restarted correctly

    def test_find_webpage(self):
        # Test the find_webpage method
        self.cmd_executor.find_webpage("OpenAI")
        # Add assertions here to check if the webpage was found correctly

if __name__ == '__main__':
    unittest.main()
