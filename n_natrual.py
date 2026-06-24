# sum of n natural numbers using recursion
x= int(input("Enter a number:"))

def sum_natural(n):
    if n==0:
        return 0
    else:
        return n+sum_natural(n-1)
print("sum is ",sum_natural(x))