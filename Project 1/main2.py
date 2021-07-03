# import random
# def game(comp,you):
#     if comp==you:
#         return None
#     elif comp =='s':
#         if you=='p':
#             return False
#         elif you=='k':
#             return True
#     elif comp =='p':
#         if you=='k':
#             return False
#         elif you=='s':
#             return True
#     elif comp =='k':
#         if you=='s':
#             return False
#         elif you=='p':
#             return True

# print("comp turn: stone(💍) paper(📃) sscissor(✂)")
# rando1=random.randint(1,3)
# print(rando1)
# if rando1==1:
#     comp='s'
# elif rando1==2:
#     comp='p'
# elif rando1==3:
#     comp='k'
# you=input("your turn:  stone(💍) paper(📃) sscissor(✂)")
# a=game(comp,you) 

# print(f"computer chosse{comp}")
# print(f"you chosse{you}")
# if a== None:
#     print("tie")
# elif a:
#     print("you win")
# else:
#     print("you lost")
import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='p':
            return False
        elif you=='k':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'p':
        if you=='k':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'k':
        if you=='s':
            return False
        elif you=='p':
            return True

print("Comp Turn: stone(💍) paper(📃) sscissor(✂)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'k'

you = input("Your Turn: stone(💍) paper(📃) sscissor(✂)")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")