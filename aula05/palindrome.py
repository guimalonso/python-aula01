from unittest import TestCase, main

def palindrome(palavra):
    return True if palavra[::-1] == palavra else False

class Teste(TestCase):
    def test_palin(self):
        self.assertEqual(palindrome('ovo'), True)
        self.assertEqual(palindrome('guilherme'), False)
        self.assertEqual(palindrome('osso'), True)
        self.assertEqual(palindrome('python'), False)

if __name__ == '__main__':
    main()