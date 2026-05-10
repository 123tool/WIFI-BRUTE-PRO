## ⚡ WIFI BRUTE PRO

**WIFI-BRUTE PRO** adalah tool audit keamanan jaringan nirkabel yang dirancang untuk pengujian penetrasi (Pentesting) pada protokol WPA2-PSK. Dikembangkan dengan arsitektur modular untuk stabilitas tinggi dan performa yang lebih agresif dibandingkan script standar.

> **Disclaimer :** Alat ini dibuat hanya untuk tujuan edukasi dan audit keamanan legal. Penggunaan pada jaringan tanpa izin adalah tindakan ilegal. **Spy-E & 123tool** tidak bertanggung jawab atas penyalahgunaan alat ini.

---

## 🛠️ Fitur Utama
* **Modular Engine:** Pemisahan logika koneksi dan UI untuk performa optimal.
* **Auto-Profile Cleanup:** Menghapus profil WiFi sampah secara otomatis untuk mencegah sistem "stuck".
* **Smart Scanning:** Deteksi SSID dan BSSID di sekitar dengan akurasi tinggi.
* **Dual-Platform Support:** Berjalan lancar di Linux (Root) dan Windows (Administrator).
* **Professional Logging:** Hasil crack disimpan otomatis di folder `data/logs.txt`.

---

## 🚀 Panduan Instalasi

## 1. Persyaratan Sistem
* Python 3.x
* Wireless Card (mendukung mode monitor/scanning)
* Akses **Root** (Linux/Termux) atau **Administrator** (Windows)

## 2. cloning
# Clone direktori ini atau extract file zip
```
cd wifi_pro
```
# Install dependencies yang dibutuhkan
```
pip install pywifi
```
## 3. Cara Penggunaan
Siapkan Wordlist : Masukkan daftar password kamu ke dalam file data/passwords.txt.
Jalankan Tool :
# Menggunakan wordlist default
```
python main.py
```
# Menggunakan wordlist custom
```
python main.py /jalur/ke/wordlist.txt
```

- Pilih Target: Pilih ID WiFi yang muncul di layar, lalu tekan Enter.
- Tunggu Proses : Biarkan engine bekerja. Jika ditemukan, password akan muncul di layar dan tersimpan di data/logs.txt.
