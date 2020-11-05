import unittest
import robot
from io import StringIO
from unittest.mock import patch
from world import obstacles

class TestObstacles(unittest.TestCase):
    @patch("sys.stdin", StringIO("OFFSET\nOff\n"))
    def test_get_obstacles(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            obstacles.num_obstacles = 0
            robot.robot_start()
        self.assertEqual(len(obstacles.get_obstacles()), 0)


    @patch("sys.stdin", StringIO("OFFSET\nOff\n"))
    def test_plot_robot_path(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            obstacles.plot_robot_path(0, 0, 0, 5)
            robot.robot_start()
        self.assertTrue(len(obstacles.robot_path), 5) 


    @patch("sys.stdin", StringIO("ROBO\nforward 20\noff\n"))
    def test_is_path_blocked(self):
        with patch('sys.stdout', new = StringIO()) as simulate_output:
            obstacles.random.randint = lambda x, y: 0
            robot.robot_start()
        self.assertEqual(obstacles.is_path_blocked(0,0,0,20), False) 
