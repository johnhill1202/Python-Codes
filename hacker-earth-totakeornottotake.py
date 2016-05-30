#To take or not to take
possible_solution=1
balloons=[]
d=""
current_answer=1
for x in range(int(input("Enter an integer: "))):
    current_answer=1
    for y in range(int(input("Enter number of balloons: "))):
        balloons.append(input("Enter balloon "+  str(y+1) + ": "))
    balloons_length=len("{0:b}".format((len(balloons)**2)-1))
    for z in range((len(balloons)**2)-1,-1,-1):
        current_answer=1
        b="{0:b}".format(z)
        for c in b:
            d = c + d
        for a in range(balloons_length):
            try:
                if(int(d[a])==1):
                    if(balloons[a]=="N"): current_answer*=-1
                    else:
                        current_answer=int(eval(str(current_answer) + balloons[a]))
            except:
                pass
        if possible_solution < current_answer:
            possible_solution = current_answer
    print("Best Answer: ", possible_solution)
    balloons=[]