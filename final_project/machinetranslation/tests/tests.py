import unittest
import sys
sys.path.append('.')
from . import translator


class TestMethods(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hola')
        self.assertEqual(translator.english_to_french(None), '')


    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(translator.english_to_french('Hello'), 'Hola')
        self.assertEqual(translator.french_to_english(None), '')


if __name__ == '__main__':
    unittest.main()