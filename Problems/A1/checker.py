def read(filename):
    with open(filename,"r") as file: return file.read()

a,b=read("A.OUT"),read(input())
print(int(a)==int(b))