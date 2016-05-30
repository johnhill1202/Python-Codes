name_1=input("Enter a string: ")
name=""
x=0
for letters in name_1:
    x+=1
for y in range(x-1,-1,-1):
    name+=name_1[y]
print(name)