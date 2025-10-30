import unittest
from main import calculoCosto

class TestEdgeCases(unittest.TestCase):
    def test_no_friends_does_not_crash(self):
        """
        Tests that the program does not crash when no friends are entered.
        """
        amigos = []
        costo_promedio = calculoCosto(amigos)
        self.assertEqual(costo_promedio, 0)

if __name__ == '__main__':
    unittest.main()
