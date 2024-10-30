import random as rd

ch = ['snake','gun','water']


while 1: #continuous the loop until the user exits
    up=0;cp=0
    x=int(input('''
                    Snake,Water,Gun Game:
                    1) Play
                    2) Exit
Enter choice : '''))
    #takes the number of rounds to play
    if(x==1):
        rounds=int(input("Enter the number of rounds to play : "))
        # TO REPEAT THE PLAYING ROUNDS
        for i in range(0,rounds):
            choice=int(input('''
                select :
                1 for Snake
                2 for Water
                3 for Gun
                choice : '''))
            # assigning random choice to the computer choice
            compC=rd.choice(ch)
            if(choice==1):
                userC="snake"
            elif(choice==2):
                userC="water"
            else:
                userC="gun"
            # if both the choices are equal then increase both of their score
            if(userC==compC):
                up+=1 # user points increase by 1
                cp+=1 # computer's points increase by 1
                print("computer choice : ",compC)
                print("your choice : ",userC)
                print("We have a draw")
            # case where the user wins
            elif(userC=="snake"and compC=="water")or(userC=="water"and compC=="gun")or(userC=="gun"and compC=="snake"):
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
            if(i==rounds-1):
                print("\n")
                # user wins
                if(up>cp):
                    print("Your points : ",up)
                    print("computer's points : ",cp)
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
