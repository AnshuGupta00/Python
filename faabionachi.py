# fibonacci series using recursion
x=int(input("Enter a number:"))

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print("Fibonacci series:" ,end="")
for i in range(x):
    print(fibonacci(i),end=" ")