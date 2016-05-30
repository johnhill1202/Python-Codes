pyramid=int(input("Enter an integer: "))
for x in range(1,pyramid+1):
    for y in range(1,x+1):
        print(y,end=" ")
    print("")