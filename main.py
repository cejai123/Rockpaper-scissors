import tkinter 
from tkinter import *
import random
from random import randint
root = Tk()
root.title("Rock Paper scissors")

playerscore =Label(root, text=0, font=100)
computerscore = Label(root, text=0,font=100)
computerscore.grid(row=1, column=1)
playerscore.grid(row=1, column=3)

personidicator = Label(root, font=50, text="USER")
computeridicator = Label(root, font=50, text="COMPUTER")
personidicator.grid(row=0, column=3)
computeridicator.grid(row=0, column=1)

message = Label(root, font=50)
message.grid(row=3, column=2)

userpick = Label(root, text="")
userpick.grid(row=3, column=3)
computer = Label(root, text="")
computer.grid(row=3, column=1)


def updateMessage(x):
    message["text"] = x

def updateuserscore():
    score = int(playerscore["text"])
    score +=1
    playerscore["text"] = str(score)

def updatecomputerscore():
    compscore = int(computerscore["text"])
    compscore +=1
    computerscore["text"] = str(compscore)

def checkwin(player, computer):
    if player == computer:
        updateMessage("Its a Tie")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updatecomputerscore()
        else:
            updateMessage("You win")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updatecomputerscore()
        else:
            updateMessage("You win")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updatecomputerscore()
        else:
            updateMessage("You win")
            updateuserscore()
    else:
        pass

choices = ["rock","paper","scissor"]
def updatechoice(x):
    compchoice = choices[randint(0,2)]
    if compchoice == "rock":
        computer.config(text="ROCK")
    elif compchoice == "paper":
        computer.config(text="PAPER")
    else:
        computer.config(text="SCISSORS")

    if x == "rock":
        userpick.config(text="ROCK")
    elif x == "paper":
        userpick.config(text="PAPER")
    else:
        userpick.config(text="SCISSORS")

    checkwin(x, compchoice)

rock = Button(root, width=20, height=2, text="ROCK",bg="#FF3E4D",fg="white", command=lambda:updatechoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",bg="#FAD02E",fg="white", command=lambda:updatechoice("paper")).grid(row=2, column=2)
Scissors = Button(root, width=20, height=2, text="SCISSORS",bg="#0ABDE3",fg="white", command=lambda:updatechoice("scissor")).grid(row=2, column=3)

root.mainloop()