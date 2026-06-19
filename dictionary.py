# car={
#     "model":"Toyota",
#     "year":2020,
#     "color":"Red"
# }

# x=car.get("model")

# print(x)

# # // Output: Toyota
# # // Set Example

# my_set={"anshu", "sacchin", "Kholi"}
# my_set2={"anshu", "sacchin", "Kholi"}

# my_set.add("Rohit")
# my_set.remove("anshu")

# result=my_set.union(my_set2)
# y="Anshu" in my_set


# print(my_set)
# # print(y)
# print(result)


# LOOPS
# i=100
# while i>=1:
#         print(i)
#         i-=1


# Table 

# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j)
#         print()


# Odd no

# for i in range (1,20):
#      if i % 2 == 1:
#         print(i)


# find the index of a number in a tuppel 
# def tuppel():
#     tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     num = int(input("Enter a Number: "))
#     n = 0
#     t=num
#     for i in tup:
#         if i == num:
#             print("Number found at index", n)
#             return
#         n = n + 1
#     print("Number is not Found")

# tuppel()


# if else 
def tuppel ():
    tup=(1,2,3,4,5)
    num=tup
    user=int (input("Enter a number:"))
    n=0
    for n, item in enumerate(tup):
        if item == user:
            print("Index is ",n)
            return 
    print("Number not Found ")

    tuppel()





