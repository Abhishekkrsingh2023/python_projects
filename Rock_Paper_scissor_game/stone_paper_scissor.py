'''
******** ROCK PAPER SCISSOR GAME **********

'''
#library for using random function
import random

l=["rock","paper","scissor"]

while 1: #continuous the loop until the user exits
    up=0;cp=0
    x=int(input('''Do you want to play the game :
                   1 YES
                   2 No | (exit)                  
                   choice : '''))
    #takes the number of rounds to play
    if(x==1):
        rounds=int(input("Enter the number of rounds to play : "))
        # TO REPEAT THE PLAYING ROUNDS
        for i in range(0,rounds):
            choice=int(input('''
                select :
                1 for rock
                2 for paper
                3 for scissor
                choice : '''))
            # assigning random choice to the computer choice
            compC=random.choice(l)
            if(choice==1):
                userC="rock"
            elif(choice==2):
                userC="paper"
            else:
                userC="scissor"
            # if both the choices are equal then increase both of their score
            if(userC==compC):
                up+=1 # user points increase by 1
                cp+=1 # computer's points increase by 1
                print("computer choice : ",compC)
                print("your choice : ",userC)
                print("We have a draw")
            # case where the user wins
            elif(userC=="rock"and compC=="scissor")or(userC=="paper"and compC=="rock")or(userC=="scissor"and compC=="paper"):
                up+=1 # user points increase by 1
                print("your choice : ",userC)
                print("computer choice : ",compC)
                print("You won")
            else:
                cp+=1 # computer's points increase by 1
                print("your choice : ",userC)
                print("computer choice : ",compC)
                print("You lose")
            # after completing the rounds
            if(i==5):
                print("\n")
                # user wins
                if(up>cp):
                    print("Your points : ",up)
                    print("cpmputer's points : ",cp)
                    print("You won this match")
                # computer wins
                elif(cp>up):
                    print("Your points : ",up)
                    print("computer's points : ",cp)
                    print("You lost this match")
                # we have a draw
                else:
                    print("Your points : ",up)
                    print("computer's points : ",cp)
                    print("We have a draw")
                print("\n")
    else:
        break
