name=input("Enter a string: ")
text=""
x=0
for letter in name:
    if(letter == "a"):
        text+="*"
    elif(letter == "e"):
        text+="3"
    elif(letter == "i"):
        text+="9"
    else:
        text+=letter
    x+=1
print(text)