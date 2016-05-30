#Randomizer
import random
student_number=[]
for x in range(30):
    if(x<10):
        student_number.append("20141000" + str(x))
    else:
        student_number.append("2014100" + str(x))
print(random.sample(student_number,1))