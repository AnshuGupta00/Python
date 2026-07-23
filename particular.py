# create a programm to find a particular word in a file.

def find_word():
    with open("C:\\Users\\gupta\\Desktop\\sample.txt.txt","r+") as f:
        content=f.read().lower()   
        # return content


    user =input("Enter the word which you want to find :").lower()

    if user in content:
        print(f"Word '{user}'found ")
    else:
        print(f"'{user}'word not found")

find_word()

