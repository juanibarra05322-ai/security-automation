#!/usr/bin/env python3
import socket
from datetime import datetime

# === CONFIG ===
TARGET = input("Target (IP o dominio): ").strip()
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}
TIMEOUT = 1

# === OUTPUT FILE ===
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"scan_result_{TARGET}_{timestamp}.txt"

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((TARGET, port))
        s.close()
        return True
    except:
        return False

print(f"\n[*] Starting basic port scan on {TARGET}\n")

results = []
for port, service in COMMON_PORTS.items():
    status = "OPEN" if check_port(port) else "CLOSED"
    results.append(f"{port} ({service}): {status}")
    print(f"{port} ({service}): {status}")

# === SAVE RESULTS ===
with open(output_file, "w") as f:
    f.write(f"Basic Port Scan Report\n")
    f.write(f"Target: {TARGET}\n")
    f.write(f"Date: {timestamp}\n\n")
    for line in results:
        f.write(line + "\n")

print(f"\n[+] Scan completed. Results saved to {output_file}")
