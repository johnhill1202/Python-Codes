class Animal():
    a_type=""
    a_legs="four"
    a_sound=""
    a_name=""    
class Dog(Animal):
    a_type="tame"
    a_sound="bark"
    a_name="Dog"
    
class Cat(Animal):
    a_type="tame"
    a_sound="meow"
    a_name="Cat"
    
class Boar(Animal):
    a_type="wild"
    a_sound="oink"
    a_name="Boar"
    
def ask():
    try:
        print("1)Dog 2)Cat 3)Boar")
        choice=int(input("Choose an animal: "))
        if choice == 1:
            action(choice)
        elif choice == 2:
            action(choice)
        elif choice == 3:
            action(choice)
        else: ask()
    except:
        ask()

def action(y):
    x=int(y)
    try:
        if x == 1: a= Dog()
        elif x == 2: a= Cat()
        else: a= Boar()
        
        print("1)Type 2)Sound 3)Number of legs")
        choice=int(input("What would you like to know about the animal?: "))
        if choice == 1: print("The ",a.a_name, " is a ",a.a_type, " animal")
        elif choice == 2: print("The ", a.a_name, "'s sound is ", a.a_sound)
        elif choice == 3: print("The ", a.a_name, " has ",a.a_legs, "legs")
        else: action(x)
    except:
        print("Hello")
ask()