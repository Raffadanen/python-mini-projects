def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

print("1. Add\n2. Sub\n3. Mul\n4. Div")
c = int(input("Choose: "))
a = float(input("A: "))
b = float(input("B: "))

ops = [add, sub, mul, div]
print("Result =", ops[c-1](a,b))
