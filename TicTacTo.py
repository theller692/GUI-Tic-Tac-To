from tkinter import *
import time

master = Tk()
Turn=StringVar()
Title = Label(master, text="Tic Tac To").grid(row=0, column=0, columnspan=5, ipadx=0)
TurnInfo = Label(master, textvariable=Turn).grid(row=1, column=0, columnspan=5, ipadx=0)

master.wm_title("Tic Tac To")
Player = 'X'

Turn.set("Turn for X.\nPlease click on a space.")

def callback():
    #Turn Cycling
    global Player
    for i in range(9):
        if Player == "O":
            Player = "X"
        else:
            Player = "O"

    Turn.set("Turn for " + Player + ".\nPlease click on a space.")



############################-=BUTTON STATE CHANGES=-################################
def TopLeft():
    TopLeft.config(state=DISABLED, relief=RAISED, text=Player)
    callback()
def TopMid():
    TopMid.config(state=DISABLED, relief=RAISED, text=Player)
    callback()
def TopRight():
    TopRight.config(state=DISABLED, relief=RAISED, text=Player)
    callback()

def MidLeft():
    MidLeft.config(state=DISABLED, relief=RAISED, text=Player)
    callback()
def MidMid():
    MidMid.config(state=DISABLED, relief=RAISED, text=Player)
    callback()
def MidRight():
    MidRight.config(state=DISABLED, relief=RAISED, text=Player)
    callback()

def BotLeft():
    BotLeft.config(state=DISABLED, relief=RAISED, text=Player)
    callback()
def BotMid():
    BotMid.config(state=DISABLED, relief=RAISED, text=Player)
    callback()
def BotRight():
    BotRight.config(state=DISABLED, relief=RAISED, text=Player)
    callback()


###############################-=TICK BOXES=-###########################################

TopLeft = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=TopLeft)
TopMid = Button(master, text=" ", width=2,relief=GROOVE,overrelief=SUNKEN, command=TopMid)
TopRight = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=TopRight)

MidLeft = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=MidLeft)
MidMid = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=MidMid)
MidRight = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=MidRight)

BotLeft = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=BotLeft)
BotMid = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=BotMid)
BotRight = Button(master, text=" ", width=2, relief=GROOVE,overrelief=SUNKEN, command=BotRight)


################################-=GRID LOCATIONS=-#######################################
TopLeft.grid(row=2, column=0)
TopMid.grid(row=2, column=2)
TopRight.grid(row=2, column=4)

MidLeft.grid(row=4, column=0)
MidMid.grid(row=4, column=2)
MidRight.grid(row=4, column=4)

BotLeft.grid(row=6, column=0)
BotMid.grid(row=6, column=2)
BotRight.grid(row=6, column=4)


################################-=DIVISOR LINES=-########################################

lineTopLeft = Label(master, text=' || \n || ', padx=0).grid(row=2, column=1)
lineTopRight = Label(master, text=' || \n || ', padx=0).grid(row=2, column=3)

topHorizontalLine = Label(master, text='==============',padx=0).grid(row=3, column=0, columnspan=5)

lineMidLeft = Label(master, text=' || \n || ', padx=0).grid(row=4, column=1)
lineMidRight = Label(master, text=' || \n || ', padx=0).grid(row=4, column=3)

bottomHorizontalLine = Label(master, text='==============',padx=0).grid(row=5, column=0, columnspan=5)

lineBotLeft = Label(master, text=' || \n || ', padx=0).grid(row=6, column=1)
lineBotRight = Label(master, text=' || \n || ', padx=0).grid(row=6, column=3)


mainloop()

