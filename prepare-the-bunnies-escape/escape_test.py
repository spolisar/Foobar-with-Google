import unittest
import solution


class VersionCompareTests(unittest.TestCase):
    # these tests are the examples that were provided in the readme
    def test_provided1(self):
        map = [[0, 0, 0, 0, 0, 0], 
               [1, 1, 1, 1, 1, 0], 
               [0, 0, 0, 0, 0, 0], 
               [0, 1, 1, 1, 1, 1], 
               [0, 1, 1, 1, 1, 1], 
               [0, 0, 0, 0, 0, 0]]
        self.assertEqual(solution.solution(map), 11)

    def test_provided2(self):
        map = [[0, 1, 1, 0], 
               [0, 0, 0, 1], 
               [1, 1, 0, 0], 
               [1, 1, 1, 0]]
        self.assertEqual(solution.solution(versions), 7)
