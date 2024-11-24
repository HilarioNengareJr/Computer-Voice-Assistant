import unittest
from src.command_processor import CommandProcessor
from src.command_execution import CommandExecution

class TestCommandProcessor(unittest.TestCase):
    def setUp(self):
        self.cmd_executor = CommandExecution()
        self.cmd_processor = CommandProcessor(self.cmd_executor)

    def test_parse_command(self):
        # Test the parse_command method
        parsed_command = self.cmd_processor.parse_command("open folder /tmp")
        # Add assertions here to check if the command was parsed correctly

    def test_do_this(self):
        # Test the do_this method
        response = self.cmd_processor.do_this("open folder /tmp")
        # Add assertions here to check if the command was processed correctly

    def test_extract_path(self):
        # Test the extract_path method
        path = self.cmd_processor.extract_path("open folder /tmp")
        # Add assertions here to check if the path was extracted correctly

    def test_extract_app_name(self):
        # Test the extract_app_name method
        app_name = self.cmd_processor.extract_app_name("open app gedit")
        # Add assertions here to check if the app name was extracted correctly

    def test_extract_query(self):
        # Test the extract_query method
        query = self.cmd_processor.extract_query("find webpage OpenAI")
        # Add assertions here to check if the query was extracted correctly

if __name__ == '__main__':
    unittest.main()
