import random

name = input("Enter Your Name to Start\n")
print("Where You want to rob first",[name])

job = input("BANK=B\nHOUSE=H\nMUSEUM=M\nJEWELLERY SHOP=J\n")



# HOUSE
if job == 'H':
    RR = (random.randrange(1,3))
    select = input("Select any number from 1 to 3\n")

    if RR == select:
        print("You Won 5000 💰😃")
    
    elif RR != select:
        print("YOU CAUGHT BY POLICE 🚔")

    else:
        pass


# MUSEUM
elif job == 'M':
    print("Hey,don't rush there are lots of trap in MUSEUM\nSo use you head and rob safely")
    print("QUSTION\nWhat word is spelled incorrectly in every single dictionary? ")
    ans = input("ENTER YOUR ANSWERE:- ")

    if ans == 'incorrectly':
        print("You are Right,YOU GOT 10000 💰😃")


    elif ans != 'incorrectly':
        print("YOU CAUGHT BY POLICE 🚔")

    else:
        pass



# JEWELLERY SHOP
elif job == 'J':
    PC = input("SELECT\nROCK🥌\nPAPER📄\nSCISSORS✂\n")
    CC = ["ROCK","PAPER","SCISSORS"]
    RC = (random.choice(CC))

    if PC == RC:
        print("YOU GOT 2 DIAMONDS💎😆")

    elif PC != RC:
        print("YOU CAUGHT BY POLICE 🚔")

    else:
        pass



# BANK
elif job =="B":
    passw = input("Guess a number of password and open door [2X70]:-\n")
    
    
  
    if passw == "9":
        print("YOU GOT 50000 💰😃")

    elif passw != "9":
        print("YOU CAUGHT BY POLICE 🚔")    
    
        

