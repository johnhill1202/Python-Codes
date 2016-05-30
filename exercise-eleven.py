def factorial(x):
    if(x==0):
        return 1
    else:
        z=1
        for y in range(1,x+1):
            z*=y
        return z
n=int(input("Enter value of N: "))
k=int(input("Enter value of K: "))
fact_n=factorial(n)
fact_k=factorial(k)
print(factorial(n)/(factorial(k)*(factorial(n-k))))