

def fib(n):
    a, b = 0, 1
    while a < n:
        yield(a)
        a, b = b, a+b


 
n = int(input("Enter Number:"))

print(list(fib(n)))