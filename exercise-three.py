names=[]
notok=True
while (notok):
    x=input("Enter a name: ")
    if(x == ""):
        notok=False
    else:
        names.append(x)
print(names)
for name in names:
    for letter in name:
        if(letter == "b"):
            print(name, " contains letter 'b'")
            break
