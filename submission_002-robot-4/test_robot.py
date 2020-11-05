import unittest
from robot import *
import sys
from io import StringIO
from unittest.mock import patch
from world import obstacles

class TestRobot(unittest.TestCase):
    @patch("sys.stdin", StringIO("OFFSET\nOff\n"))
    def test_name_of_robot(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            robot_start()
        self.assertEqual("""What do you want to name your robot? OFFSET: Hello kiddo!
OFFSET: What must I do next? OFFSET: Shutting down..\n""", simulate_output.getvalue())


    @patch("sys.stdin", StringIO("OFFSET\nOfF\n"))
    def test_off_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            robot_start()
        self.assertEqual("""What do you want to name your robot? OFFSET: Hello kiddo!
OFFSET: What must I do next? OFFSET: Shutting down..\n""", simulate_output.getvalue())


    @patch("sys.stdin", StringIO("OFFSET\nRun\nOff"))
    def test_valid_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            robot_start()
        self.assertEqual("""What do you want to name your robot? OFFSET: Hello kiddo!
OFFSET: What must I do next? OFFSET: Sorry, I did not understand 'Run'.
OFFSET: What must I do next? OFFSET: Shutting down..\n""", simulate_output.getvalue())


    @patch("sys.stdin", StringIO("QUAVO\nheLP\noff\n"))
    def test_help_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            robot_start()
        self.assertEqual("""What do you want to name your robot? QUAVO: Hello kiddo!
QUAVO: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
""", simulate_output.getvalue()[:520])


    @patch("sys.stdin", StringIO("ROBO\nfORward 10\noff\n"))
    def test_forward_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            robot_start()
        self.assertEqual("""What do you want to name your robot? ROBO: Hello kiddo!
ROBO: What must I do next?  > ROBO moved forward by 10 steps.
 > ROBO now at position (0,10).
ROBO: What must I do next? ROBO: Shutting down..\n""", simulate_output.getvalue())


    @patch("sys.stdin", StringIO("ROBO\nBack 10\noff\n"))
    def test_back_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            obstacles.random.randint = lambda x, y: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? ROBO: Hello kiddo!
ROBO: What must I do next?  > ROBO moved back by 10 steps.
 > ROBO now at position (0,-10).
ROBO: What must I do next? ROBO: Shutting down..\n""", simulate_output.getvalue())


    @patch("sys.stdin", StringIO("ROBO\nright\nForward 10\noff\n"))
    def test_right_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            obstacles.random.randint = lambda x, y: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? ROBO: Hello kiddo!
ROBO: What must I do next?  > ROBO turned right.
 > ROBO now at position (0,0).
ROBO: What must I do next?  > ROBO moved forward by 10 steps.
 > ROBO now at position (10,0).
ROBO: What must I do next? ROBO: Shutting down..\n""", simulate_output.getvalue())


    @patch("sys.stdin", StringIO("ROBO\nLeft\nForward 15\noff\n"))
    def test_left_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            obstacles.random.randint = lambda x, y: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? ROBO: Hello kiddo!
ROBO: What must I do next?  > ROBO turned left.
 > ROBO now at position (0,0).
ROBO: What must I do next?  > ROBO moved forward by 15 steps.
 > ROBO now at position (-15,0).
ROBO: What must I do next? ROBO: Shutting down..\n""", simulate_output.getvalue())


    @patch("sys.stdin", StringIO("ROBO\nsprint 5\noff\n"))
    def test_sprint_command(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            obstacles.random.randint = lambda x, y: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? ROBO: Hello kiddo!
ROBO: What must I do next?  > ROBO moved forward by 5 steps.
 > ROBO moved forward by 4 steps.
 > ROBO moved forward by 3 steps.
 > ROBO moved forward by 2 steps.
 > ROBO moved forward by 1 steps.
 > ROBO now at position (0,15).
ROBO: What must I do next? ROBO: Shutting down..\n""", simulate_output.getvalue())