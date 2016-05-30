numbers=[]
while(True):
    x=input("Enter a number: ")
    if (x != ""):
        numbers.append(int(x))
    else:
        break
for number in numbers:
    print(number if number < 0 else "")