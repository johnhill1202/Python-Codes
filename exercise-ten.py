x=int(input("Enter an integer: "))
print("Not Weird" if (x%2 == 0) and ((x>1 and x < 5) or (x > 21)) else "Weird")