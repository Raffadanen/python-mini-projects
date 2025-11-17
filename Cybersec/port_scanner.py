import socket

target = input("Target IP: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    s.close()

print("\nScan complete.")
