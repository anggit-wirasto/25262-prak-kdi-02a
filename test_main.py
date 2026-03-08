# test_main.py
import unittest
from main import caesar_cipher

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        """Test enkripsi huruf kecil dasar"""
        self.assertEqual(caesar_cipher("abc", 5), "fgh")

    def test_decrypt_basic(self):
        """Test dekripsi huruf kecil dasar"""
        self.assertEqual(caesar_cipher("fgh", 5, mode='decrypt'), "abc")

    def test_encrypt_with_spaces_and_punctuation(self):
        """Test enkripsi dengan spasi, huruf besar, dan tanda baca"""
        self.assertEqual(caesar_cipher("Halo, Dunia!", 5), "Mfqt, Izsnf!")

    def test_decrypt_with_spaces_and_punctuation(self):
        """Test dekripsi dengan spasi, huruf besar, dan tanda baca"""
        self.assertEqual(caesar_cipher("Mfqt, Izsnf!", 5, mode='decrypt'), "Halo, Dunia!")

    def test_secret_decipher(self):
        """
        SECRET TEST: Menguji apakah mahasiswa bisa memecahkan pesan 
        'bukti fraud di server b'
        """
        ciphertext = "gzpyn kwfzi in xjawjw g"
        expected_plaintext = "bukti fraud di server b"
        
        hasil = caesar_cipher(ciphertext, 5, mode='decrypt')
        self.assertEqual(hasil, expected_plaintext, "Gagal mendecipher pesan rahasia fraud server!")

if __name__ == '__main__':
    unittest.main()