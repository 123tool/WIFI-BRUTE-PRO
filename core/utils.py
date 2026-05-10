import os
import sys
import platform

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def check_root():
    if platform.system() != "Windows":
        if os.geteuid() != 0:
            print("\n[!] Error: Akses Root/Sudo diperlukan untuk kontrol interface WiFi.")
            sys.exit()

def get_wordlist(path):
    if not os.path.exists(path):
        print(f"\n[!] Error: File {path} tidak ditemukan!")
        sys.exit()
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return [line.strip() for line in f if line.strip()]
