'''
************** PROGRAM TO FIND A SPY NUMBER **************
'''
''' 
NOTE : A SPY number is a number where the sum
          of digits is equal to the product of the 
          digits
'''
# loop for continuing the game
def sum(a):
    add=0
    while(a!=0):
        add+=(a%10);
        a//=10
    return add;

def product(a):
    pro=1;
    while(a!=0):
        pro*=(a%10);
        a//=10;
    return pro;

while(True):
    print('''
        press 1 to play :
        press 2 to exit :

      ''')
    op=int(input("Enter your choice : "))
    if(op==1):
        print("The GAME has Began!!!!")
        # user choice 
        num=int(input("Enter the number :"))

        # print(sum(num))
        if(sum(num)==product(num)):
            print("Correct guess , YOU WIN")
        else:
            print("Wrong guess , Better luck next time")
    else:
        break;