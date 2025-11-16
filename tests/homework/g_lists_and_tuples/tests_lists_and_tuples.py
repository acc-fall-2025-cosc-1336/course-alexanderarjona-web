import unittest
from src.homework.lists_and_tuples.lists import get_p_distance
from src.homework.lists_and_tuples.lists import get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        l1 = ['T','T','T','C','C','A','T','T','T','A']
        l2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertAlmostEqual(get_p_distance(l1, l2), 0.4, places=3)

    def test_get_p_distance_matrix(self):
        data = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]

        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]

        result = get_p_distance_matrix(data)
        self.assertEqual(result, expected)
