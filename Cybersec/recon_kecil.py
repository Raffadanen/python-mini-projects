import socket
import hashlib

def scan_port(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
        return True
    except:
        return False

def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

print("Scanning google.com:80 =", scan_port("google.com", 80))
