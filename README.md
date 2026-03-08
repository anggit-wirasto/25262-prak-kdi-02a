# Praktikum Keamanan Data dan Informasi: Caesar Cipher

**Universitas Harapan Bangsa** **Mata Kuliah:** Keamanan Data dan Informasi  
**Dosen Pengampu:** Anggit Wirasto, S.Si., M.Eng.

---

## 🎯 Tujuan Praktikum
Pada praktikum ini, Anda diminta untuk mengimplementasikan algoritma kriptografi klasik **Caesar Cipher** menggunakan bahasa pemrograman Python. Program yang Anda buat harus mampu melakukan dua mode: **Enkripsi (Encrypt)** dan **Dekripsi (Decrypt)** dengan nilai pergeseran (*shift*) tertentu.

## 📝 Instruksi Tugas
Lengkapi fungsi `caesar_cipher` yang terdapat di dalam file `main.py`. Gunakan pedoman *pseudocode* berikut sebagai alur logika dasar Anda:

```text
FUNGSI caesar_cipher(teks, geser, mode[default: 'encrypt']):
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
  ```

## Ketentuan Tambahan:

- Anda hanya diperbolehkan mengubah kode di dalam file main.py.
- Program harus bisa menangani spasi, tanda baca, huruf besar, dan huruf kecil dengan benar.
- Nilai pergeseran (shift) default untuk pengujian di sistem ini adalah 5.

<!-- ## Cara Menguji Kode Anda Secara Lokal
Sebelum melakukan git push untuk dinilai oleh sistem, sangat disarankan untuk menguji kode Anda sendiri di terminal/CMD laptop Anda.

Jalankan perintah berikut di direktori proyek ini:

```bash
python -m unittest test_main.py
``` -->