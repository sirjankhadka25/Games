import subprocess
import re

def parse_arp_windows():
    out = subprocess.check_output("arp -a", shell=True, text=True)
    # lines like:  192.168.1.10       00-11-22-33-44-55     dynamic
    devices = []
    for line in out.splitlines():
        m = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\-]{17})\s+(\w+)", line)
        if m:
            ip, mac, kind = m.groups()
            mac = mac.replace('-', ':').lower()
            devices.append({"ip": ip, "mac": mac, "type": kind})
    return devices

if __name__ == "__main__":
    devices = parse_arp_windows()
    print("ARP table devices:")
    for d in devices:
        print(f"{d['ip']}  |  {d['mac']}  |  {d['type']}")
