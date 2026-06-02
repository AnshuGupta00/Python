def tuppel():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    num = int(input("Enter a Number: "))

    n = 0
    for i in tup:
        if i == num:
            print("Number found at index", n)
            return
        n = n + 1

    print("Number is not Found")

tuppel()

  
