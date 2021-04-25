import random
r=random.randint(1,100)
guess=0
num=None
while(num!=r):
    num=int(input("Enter a number"))
    guess+=1
    def lh():
        if(num>r):
            print("Lower number please")
        elif(num<r):
            print("Higher number pelase")
        else:
            print("You guessed it right!! You required",guess,"guesses")
    lh()
