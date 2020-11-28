#Buddy
version="1.0"
#Created by Jura Perić

#Modules
from time import*
from turtle import*
from random import*
from datetime import*

#Variables
calcNum1=0
calcNum2=0
secNum=0
correctExecution=False
processName=""

#Lists
flipCoin=["Heads.", "Tails."]

#Main code
print("Hello! I'm Buddy! How can I help you?")
while True: #Executes forever
    #Resets some important variables
    correctExecution=False
    processName=""
    #Asks the user for an input
    userInput=input("{}>>>".format(processName))

    #Lists all commands
    if userInput.find("help")>=0:
        print("All commands: ")
        print("how are you")
        print("pick a random number")
        print("flip a coin")
        print("calculate")
        print("start a timer")
        print("what's the time")
        print("Be a part of the project and contribute to Buddy on GitHub: https://github.com/JuraPwasTaken/Buddy")
        correctExecution=True

    #Healthy and positive interaction
    if userInput.find("how" and "you")>=0:
        print("Pretty well.")
        correctExecution=True

    #Pick a random number
    if userInput.find("pick" and "number")>=0:
        print("{}.".format(randint(1,100)))
        correctExecution=True

    #Flip a coin
    if userInput.find("flip" and "coin")>=0:
        print(choice(flipCoin))
        correctExecution=True

    #Starts the calculator
    if userInput.find("calculate")>=0:
        processName="CALCMODE"
        userInput=input("{}>>>".format(processName))
        if userInput.find("help")>=0:
            print("Addition: +")
            print("Subtraction: -")
            print("Multiplication: *")
            print("Division: /")
        else:
            #Addition
            if userInput.find("+")>=0:
                calcNum1=int(input("Number 1: "))
                calcNum2=int(input("Number 2: "))
                print("{} + {} = {}".format(calcNum1, calcNum2, calcNum1+calcNum2))
                correctExecution=True

            #Subtraction
            if userInput.find("-")>=0:
                calcNum1=int(input("Number 1: "))
                calcNum2=int(input("Number 2: "))
                print("{} - {} = {}".format(calcNum1, calcNum2, calcNum1-calcNum2))
                correctExecution=True

            #Multiplication
            if userInput.find("*")>=0:
                calcNum1=int(input("Number 1: "))
                calcNum2=int(input("Number 2: "))
                print("{} x {} = {}".format(calcNum1, calcNum2, calcNum1*calcNum2))
                correctExecution=True

            #Division
            if userInput.find("/")>=0:
                calcNum1=int(input("Number 1: "))
                calcNum2=int(input("Number 2: "))
                print("{} ÷ {} = {}".format(calcNum1, calcNum2, calcNum1/calcNum2))
                correctExecution=True

            #Executes this if the userInput doesn't match with anything and if correctExecution is still false
            else:
                if correctExecution==False:
                    print("Sorry, but I didn't understand your command. Quitting {}...".format(processName))

    #Starts the timer
    if userInput.find("timer")>=0:
        processName="TIMER"
        userInput=input("{}>>>".format(processName))
        if userInput.find("help")>=0:
            print("You can type:")
            print('"minute"')
            print('"second"')
            print('"hour"')
        else:
            #Timer for seconds
            if userInput.find("second")>=0:
                secNum=int(input("Enter the amount of seconds: "))
                for i in range(secNum):
                    print(secNum)
                    secNum=secNum-1
                    sleep(1)
                    if secNum==0:
                        print("Time's up! Quitting TIMER...")
                        correctExecution=True

            #Timer for minutes
            if userInput.find("minute")>=0:
                secNum=int(input("Enter the amount of minutes: "))
                secNum=secNum*60
                for i in range(secNum):
                    print(secNum)
                    secNum=secNum-1
                    sleep(1)
                    if secNum==0:
                        print("Time's up! Quitting TIMER...")
                        correctExecution=True

            #Timer for hours
            if userInput.find("hour")>=0:
                secNum=int(input("Enter the amount of hours: "))
                secNum=secNum*600
                for i in range(secNum):
                    print(secNum)
                    secNum=secNum-1
                    sleep(1)
                    if secNum==0:
                        print("Time's up! Quitting TIMER...")
                        correctExecution=True

            #Executes this if the userInput doesn't match with anything and if correctExecution is still false
            else:
                if correctExecution==False:
                    print("Sorry, but I didn't understand your command. Quitting {}...".format(processName))

    #Checks the time for you
    if userInput.find("what" and "time")>=0:
        now=datetime.now()
        print("It's currently {}.".format(now.strftime("%H:%M:%S")))
        correctExecution=True

    #The prototype of this program was made in 2019 hope that explains it
    if userInput.find("creeper")>=0:
        f=open("/home/pi/Documents/Buddy/ssssssssssssssssssss.txt", "r")
        print(f.read())
        correctExecution=True

    #Executes this if the userInput doesn't match with anything and if correctExecution is still false
    else:
        if correctExecution==False:
            print("Sorry, but I didn't understand your command.")
