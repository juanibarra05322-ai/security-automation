#!/usr/bin/env python3
import socket
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Basic port scanning automation")
parser.add_argument("target", help="Target IP or domain")
args = parser.parse_args()

TARGET = args.target
TIMEOUT = 1

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"scan_{TARGET}_{timestamp}.txt"

def is_open(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((TARGET, port))
        s.close()
        return True
    except:
        return False

print(f"\n[+] Scanning {TARGET}\n")

with open(output_file, "w") as f:
    f.write(f"Target: {TARGET}\n")
    f.write(f"Date: {timestamp}\n\n")

    for port, service in COMMON_PORTS.items():
        status = "OPEN" if is_open(port) else "CLOSED"
        line = f"{port} ({service}) → {status}"
        print(line)
        f.write(line + "\n")

print(f"\n[✓] Results saved to {output_file}")
