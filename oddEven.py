# printing odd no of line in a file 

def print_line():
    with open(r"C:\Users\gupta\Desktop\sample.txt.txt","r") as f:
              for line_no, line in enumerate(f, start=1):
                if line_no %2 != 0:
                    print(line_no)
                    print(line)
print_line()