import unittest
from src.palindrome import is_palindrome 

class TestPalindrome(unittest.TestCase):
    
    def test_palabras_palindromas(self):
        self.assertTrue(is_palindrome("oso"))
        self.assertTrue(is_palindrome("anilina"))
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("arenera"))

    def test_frases_palindromas(self):
        self.assertTrue(is_palindrome("La ruta natural"))
        self.assertTrue(is_palindrome("Sé verlas al revés"))
        self.assertTrue(is_palindrome("Yo hago yoga hoy"))
        self.assertTrue(is_palindrome("Somos o no somos"))



