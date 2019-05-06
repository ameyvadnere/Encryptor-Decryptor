# Tic Tac Toe Program:
import time
print("Welcome to the Tic Tac Toe program")
time.sleep(0.5)
print("Player 1 : 1")
time.sleep(0.5)
print("Player 2: 2")

print("This is the Tic Tac Toe board:")

print ("__|__|__")
print ("__|__|__")
print ("    |    |    ")

time.sleep(2)

print("\n Each player has to input the position in the grid(1-9)")
time.sleep(2)
print("\nPlayer 1, Begin the game.")

x1,x2,x3,x4,x5,x6,x7,x8,x9 = 0,0,0,0,0,0,0,0,0

def ttc(x1,x2,x3,x4,x5,x6,x7,x8,x9):
    #def turnp1():
    #if x1*x2*x3 !=  and x4*x5*x6 != 1 and x7*x8*x9 != 1 and x1*x4*x7 != 1 and x2*x5*x8 != 1 and x3*x6*x9 != 1 and x1*x5*x9 !=1 and x3*x5*x7 != 1:
    p1 = int(input("Player 1, your turn:"))
    if p1 == 1 and x1 == 0:
        x1 = 1
    elif p1 == 2 and x2 == 0:
        x2 = 1
    elif p1 == 3 and x3 == 0:
        x3 = 1
    elif p1 == 4 and x4 == 0:
        x4 = 1
    elif p1 == 5 and x5 == 0:
        x5 = 1
    elif p1 == 6 and x6 == 0:
        x6 = 1
    elif p1 == 7 and x7 == 0:
        x7 = 1
    elif p1 == 8 and x8 == 0:
        x8 = 1
    elif p1 == 9 and x9 == 0:
        x9 = 1
    else:
        print("Invalid move.")
        #turnp1()

    print("The board configuration is:")
    print(x1,  "|",  x2 , "|" , x3)
    print(x4, "|",  x5,  "|", x6)
    print(x7, "|",  x8, "|", x9)
    
    
    if  x1*x2*x3 != 1 and x4*x5*x6 != 1 and x7*x8*x9 != 1 and x1*x4*x7 != 1 and x2*x5*x8 != 1 and x3*x6*x9 != 1 and x1*x5*x9 !=1 and x3*x5*x7 != 1:
        p2 = int(input("Your Turn, Player 2:"))
        if p2 == 1 and x1 == 0:
            x1 = 2
        elif p2 == 2 and x2 == 0:
            x2 = 2
        elif p2 == 3 and x3 == 0:
            x3 = 2
        elif p2 == 4 and x4 == 0:
            x4 = 2
        elif p2 == 5 and x5 == 0:
            x5 = 2
        elif p2 == 6 and x6 == 0:
            x6 = 2
        elif p2 == 7 and x7 == 0:
            x7 = 2
        elif p2 == 8 and x8 == 0:
            x8 = 2
        elif p2 == 9 and x9 == 0:
            x9 = 2
        else:
            print("Invalid move.")
            #turnp2()

        print("The board configuration is:")
        print(x1 , "|", x2, "|", x3)
        print(x4, "|", x5, "|", x6)
        print(x7, "|", x8, "|", x9)

        if x1*x2*x3 != 8 and x4*x5*x6 != 8 and x7*x8*x9 != 8 and x1*x4*x7 != 8 and x2*x5*x8 != 8 and x3*x6*x9 != 8 and x1*x5*x9 !=8 and x3*x5*x7 != 8:
            ttc(x1,x2,x3,x4,x5,x6,x7,x8,x9)
        else:
            print("Player 2 wins, Congrats")

    else:
        print("Player 1 wins, Congrats")

ttc(x1,x2,x3,x4,x5,x6,x7,x8,x9)
