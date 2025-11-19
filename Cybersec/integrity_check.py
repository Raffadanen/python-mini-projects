import hashlib

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        chunk = f.read(4096)
        while chunk:
            h.update(chunk)
            chunk = f.read(4096)
    return h.hexdigest()

file = input("File path: ")
original_hash = input("Original SHA256: ")

current_hash = sha256_file(file)

if current_hash == original_hash:
    print("[SAFE] File has not been modified.")
else:
    print("[WARNING] File integrity failed!")
