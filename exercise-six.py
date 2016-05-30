pyramid=int(input("Enter an integer: "))
for x in range(1,pyramid+1):
    for z in range(x,pyramid+1):
        print(" ",end="")
    for y in range(1,x+1):
        print(y,end=" ")
    print("")