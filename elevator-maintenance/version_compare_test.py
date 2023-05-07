import unittest
import solution


class VersionCompareTests(unittest.TestCase):
    # these tests are the examples that were provided in the readme
    def test_provided1(self):
        versions = ["1.11", "2.0.0", "1.2",
                    "2", "0.1", "1.2.1", "1.1.1", "2.0"]
        results = ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
        self.assertEqual(solution.solution(versions), results)

    def test_provided2(self):
        versions = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
        results = ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
        self.assertEqual(solution.solution(versions), results)
