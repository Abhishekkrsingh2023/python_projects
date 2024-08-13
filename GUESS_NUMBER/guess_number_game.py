'''
*************** GUESS THE NUMBER GAME ****************
'''

import random 

while(True):
    print('''
            Play the game guess the number ?
            1 (yes)
            2 (no) [exit] :
            ''')
    x=int (input("Enter your Choice : "))
    cnt = 1
    if(x==1):
        # generates random number between 1 to 100
        number = random.randint(1,100)
        choice=int(input("Enter a number between (1 - 100) : "))
        # if the user choice is equal to the generated number
        if(choice==number):
            print(f"Hurray!! you guessed the right number")
        else:
            # check for the number
            while(True):
                if(choice<number):
                    cnt = cnt + 1
                    choice=int(input("Emm...a bit higher :"))
                elif(choice>number):
                    cnt = cnt + 1
                    choice=int(input("Emm.. a little lower : "))
                else:
                    #if the choice matches with the number then break
                    print("Hurray!! you guessed the right number in {cnt} Trials")
                    break
    else:
        break