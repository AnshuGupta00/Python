
# create a list of natural numbers, filter even numbers, and print the even list
numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
