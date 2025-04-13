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

    def test_casos_no_palindromos(self):
        self.assertFalse(is_palindrome("Hola Mundo"))
        self.assertFalse(is_palindrome("Python es genial"))
        self.assertFalse(is_palindrome("Hoy es lunes"))
        self.assertFalse(is_palindrome("Somos o no"))

    def test_casos_edge(self):
        self.assertTrue(is_palindrome(""))  
        self.assertTrue(is_palindrome(" "))  
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("$%"))  
        self.assertTrue(is_palindrome("12321"))  
        self.assertFalse(is_palindrome("12345"))  
        self.assertTrue(is_palindrome("!"))  


