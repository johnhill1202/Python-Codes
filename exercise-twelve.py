a=int(input("Enter an integer:"))
b=0
for x in str(a):
    b+=int(x)**3
print("Armstrong Number" if(b==a) else "Not an Armstrong number")