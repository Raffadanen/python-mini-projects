import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
length = int(input("Length: "))
print("Password:", "".join(random.choice(chars) for _ in range(length)))
