import hashlib

hash_input = input("Hash: ")
wordlist = input("Wordlist file: ")

with open(wordlist, "r") as f:
    for word in f:
        word = word.strip()
        if hashlib.md5(word.encode()).hexdigest() == hash_input:
            print(f"[FOUND] {word}")
            break
    else:
        print("Not found.")
