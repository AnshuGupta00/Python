# find the no of vowels in a file
def count_vowels():
    with open(r"C:\Users\gupta\Desktop\sample.txt.txt","r") as f:
        content =f.read()
        vowels="aeiouAEIOU"
        count=0

        for char in content:
            if char in vowels:
                count+=1

        print("The no of vowels in the file is :", count)


count_vowels()


