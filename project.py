import os, time

def slowText(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

def start():
    global playerName
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Welcome to the game! Please enter your name: ")
    playerName = input()
    slowText("Hello, {}! You find yourself in the living room of a mysterious house.".format(playerName))
    slowText("From here, you can go to the kitchen, the bedroom, or the garden.")
    # Further game logic would go here
    livingRoom()

def livingRoom():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden.")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    else:
        print("Invalid choice. Please try again.")
        livingRoom()

playerName = ""
start()