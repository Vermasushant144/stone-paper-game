# game = stone paper sicsor
import random
def gamewin(computer,you):
    if computer == you:
        return None
    elif computer == "s":
        if you == "ss":
            return False
        elif you == "p":
            return True 
    elif computer == "p":
        if you == "s":
            return False
        elif you == "ss":
            return True 
    elif computer == "ss":
        if you == "p":
            return False
        elif you == "s":
            return True                        
print("computer turn : stone(s),paper(p),sicsor(ss)")
randomno = random.randint(1,3)
if randomno == 1:
    computer = "s"
elif randomno == 2:
    computer = "p"
elif randomno == 3:
    computer = "ss"
you = input("yours turn : stone(s),paper(p),sicsor(ss) ")  
a = gamewin(computer,you)  
if a == None:
    print("game is tiel")
elif a :
    print("game is win")
else:
    print("game is loose")        