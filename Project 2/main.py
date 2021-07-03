import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))


# import random
# randNumber=random.randint(1,100)
# # print(randNumber)
# useGueass=None
# guesess=0
# while(useGueass!=randNumber):
#         useGueass=int(input("enter your gues"))
#         guesess+=1
#         if(useGueass==randNumber):
#             print("you Guess it rigth")
#         else:
#             if(useGueass<randNumber):
#                 print("you gueass wrong!,enter small vlue")
#             else:
#                 print("you gues wrong!,Enter a largest no ")    

# print(f"you gues the no in{guesess} guesses")
# with open("hiscore.txt","r") as f:
#     hiscore=int(f.read())
 
# if (guesess<hiscore):
#     print("broken the highscore")
# with open("hiscore.txt","w") as f:
#     f.write(str(guesess))