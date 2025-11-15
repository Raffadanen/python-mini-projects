def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Factorial(5):", factorial(5))
print("Fibonacci(6):", fibonacci(6))
print("Prime 13:", is_prime(13))

