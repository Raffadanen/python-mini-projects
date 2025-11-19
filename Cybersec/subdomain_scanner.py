import socket

domain = input("Target domain: ")
wordlist = input("Wordlist file: ")

print("\nScanning...\n")

with open(wordlist, "r") as f:
    for sub in f:
        sub = sub.strip()
        test = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(test)
            print(f"[FOUND] {test} → {ip}")
        except:
            pass
