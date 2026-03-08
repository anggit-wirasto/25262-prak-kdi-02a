# main.py

def caesar_cipher(teks, geser, mode='encrypt'):
    """
    Fungsi untuk melakukan enkripsi atau dekripsi menggunakan Caesar Cipher.
    
    PSEUDOCODE:
    inisialisasi hasil = string kosong
    
    JIKA mode = 'decrypt':
        geser = -geser
    
    UNTUK setiap karakter DALAM teks:
        JIKA karakter adalah huruf (alpha):
            TENTUKAN ascii_offset:
                - 65 untuk huruf BESAR
                - 97 untuk huruf kecil
            substitusi = (kode_ASCII(karakter) - ascii_offset + geser) MOD 26 + ascii_offset
            karakter_baru = karakter_dari_ASCII(substitusi)
            tambahkan karakter_baru ke hasil
        SELAIN ITU:
            tambahkan karakter ke hasil (spasi dan tanda baca tetap)
    
    KEMBALIKAN hasil
    """
    
    # TULIS KODE ANDA DI BAWAH INI
    pass

# Blok di bawah ini opsional, hanya untuk memudahkan mahasiswa 
# mencoba kode mereka sendiri di terminal lokal sebelum di-push.
if __name__ == '__main__':
    print("=== Uji Coba Lokal ===")
    pesan = "Halo Dunia!"
    enkripsi = caesar_cipher(pesan, 5, 'encrypt')
    print(f"Enkripsi dari '{pesan}': {enkripsi}")
    # Hasil seharusnya: "Mfqt Izsnf!"