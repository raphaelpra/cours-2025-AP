# test_vigenere.py
import unittest
from vigenere import vigenere


class TestVigenere(unittest.TestCase):

    def test_encode_basic_example(self):
        """Test the main example from spec: encoding 'lemessage' with key 'cle'"""
        result = vigenere("lemessage", "cle", encode=True)
        self.assertEqual(result, "oqrhexdsj")

    def test_decode_basic_example(self):
        """Test the main example from spec: decoding 'oqrhexdsj' with key 'cle'"""
        result = vigenere("oqrhexdsj", "cle", encode=False)
        self.assertEqual(result, "lemessage")

    def test_encode_decode_roundtrip(self):
        """Test that encode then decode returns original"""
        original = "bonjour le monde"
        key = "secret"
        encoded = vigenere(original, key, encode=True)
        decoded = vigenere(encoded, key, encode=False)
        self.assertEqual(decoded, original)

    def test_single_character(self):
        """Test encoding a single character"""
        result = vigenere("a", "a", encode=True)
        self.assertEqual(result, "b")

    def test_non_alphabetic_preserved(self):
        """Test that spaces and numbers are not modified"""
        result = vigenere("hello 123 world", "key", encode=True)
        self.assertIn(" ", result)
        self.assertIn("123", result)

    def test_uppercase_converted(self):
        """Test that uppercase is converted to lowercase"""
        result = vigenere("HELLO", "cle", encode=True)
        self.assertTrue(result.islower())

    def test_empty_string(self):
        """Test encoding empty string"""
        result = vigenere("", "cle", encode=True)
        self.assertEqual(result, "")

    def test_default_encode_parameter(self):
        """Test that encode defaults to True"""
        result1 = vigenere("lemessage", "cle")
        result2 = vigenere("lemessage", "cle", encode=True)
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()