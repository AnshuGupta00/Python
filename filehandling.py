# file read and write
with open("C:\\Users\\gupta\\Desktop\\sample.txt.txt", "r") as f:
    content = f.read()
    print(content)

with open("C:\\Users\\gupta\\Desktop\\sample.txt.txt", "w") as f:
    content = f.write("hello world")
    print(f"characters written: {content}")