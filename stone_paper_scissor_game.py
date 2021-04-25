import random
def game(comp,you):
    if(comp==you):
        return None
    if(comp=='s' and you=='p'):
        return True
    if(comp=='s' and you=='sc'):
        return False
    if(comp=='p' and you=='s'):
        return False
    if(comp=='p' and you=='sc'):
        return True
    if(comp=='sc' and you=='s'):
        return True
    if(comp=='sc' and you=='p'):
        return False

you=input("Choose: Stone(s), Paper(p), Scissors(sc)\n")
rnum=random.randint(1,3)
print("You chose: "+you)
if(rnum==1):
    comp='s'
if(rnum==2):
    comp='p'
if(rnum==3):
    comp='sc'
print("Computer chose: "+comp)
a=game(comp,you)
if(a==False):
    print("You lose:(")
elif(a==None):
    print("It's a tie!")
else:
    print("You win:)")