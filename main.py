import random
choices = ["rock","paper","scissors"]

def getcchoices():
    return random.choice(choices)

def pchoice():
    print("choose rock paper or scissors")
    playerinput = input("your choice")
    while playerinput not in choices:
        print("Invalid choice")
        playerinput = input("your choice")
    return playerinput

def findwiner(playerinput, computerinput):
    if playerinput == computerinput:
        return("tie")
    elif(playerinput== "rock" and computerinput=="scissors") or (playerinput=="paper" and computerinput=="rock") or (playerinput=="paper" and computerinput=="rock")or(playerinput=="scissors" and computerinput=="paper"):
        return "you win"
    else:
        return "computer win"
    

def playgame():
    computerinput = getcchoices()
    playerinput  =  pchoice()
    print("computer choice is", computerinput)
    result=findwiner(playerinput, computerinput)
    print(result)
playgame()