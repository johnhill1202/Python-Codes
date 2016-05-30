prelim = float(input("Enter prelim grade: "))
midterm = float(input("Enter midterm grade: "))
final = float(input("Enter final term grade: "))
sem = prelim *.3 + midterm *.3 + final *.4
print ("Sem grade: " , sem)
print ("passed" if sem >=70 else "failed")
