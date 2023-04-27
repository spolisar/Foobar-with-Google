import unittest
import solution


class KnightTests(unittest.TestCase):
    def test_provided1(self):
        self.assertEqual(solution.solution(19, 36), 1)
    
    def test_provided2(self):
        self.assertEqual(solution.solution(0, 1), 3)