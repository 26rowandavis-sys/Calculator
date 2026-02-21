# os gives us access to the command line, time is used as a delay
import os, time

# this function prints text delayed like older video games
def slowText(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

# introduces the player, sets the playerName variable
def start():
    global playerName   # establishes playerName as a global variable
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Welcome to the game! Please enter your name: ")
    playerName = input()
    slowText("Hello, {}! You find yourself in the living room of a mysterious house.".format(playerName))
    slowText("From here, you can go to the kitchen, the bedroom, or the garden.")
    # Further game logic would go here
    livingRoom()

# continuation of the start, allows for the player to go to the living room
def livingRoom():
    global backpack
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the living room. There are doors to the kitchen, bedroom, and garden. You can also look for items")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "kitchen":
        kitchen()
    elif choice == "bedroom":
        bedroom()
    elif choice == "garden":
        garden()
    elif choice == "look for items":
        if searchBackpack(backpack, "oreos"):
            slowText("You decided to scan the room. And youfound nothing.")
        slowText("You decided to scan the room. You find a half-eaten pack of oreos. Do you want to pick them up?")
        choice = input().strip().lower()    
        if choice == "yes":  
            backpack.append ("oreos")
            print (backpack)
            time.sleep(2) 
        livingRoom ()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        livingRoom()

def kitchen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the kitchen. There is a door to the living room and a window outside. You can also look for items")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    elif choice == "open window":
        openWindow()
    elif choice == "look for items":
        if searchBackpack(backpack, "paper clip"):
            slowText("You decided to scan the room. And you found nothing.")
        slowText("You decided to scan the room. You open up a junk drawer and find a paper clip. Do you want to pick them up? ")
        choice = input().strip().lower()    
        if choice == "yes":  
            backpack.append ("paper clip")
            print (backpack)
            time.sleep(2) 
        livingRoom ()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        kitchen()

#
def garden():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the garden. There is a door to the living room. You can also look for items. ")
    slowText("What would you like to do?")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
        if searchBackpack(backpack, "oreos"):
            slowText("You decided to scan the room. And you found nothing.")
        slowText("You decided to scan the room. You found a bloody trowel. Do you want to pick them up? ")
        choice = input().strip().lower()    
        if choice == "yes":  
            backpack.append ("bloody trowel ")
            print (backpack)
            time.sleep(2) 
        livingRoom ()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        garden()

def bedroom():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("backpack: {}".format(backpack))
    slowText("You are in the bedroom. There is a door to the living room. You can also scan the room ")
    slowText("What would you like to do ")
    choice = input().strip().lower()
    if choice == "living room":
        livingRoom()
    elif choice == "look for items":
        if searchBackpack(backpack, "oreos"):
            slowText("You decided to scan the room. And you found nothing.")
        slowText("You decided to scan the room. You open up a dresser drawer and find an old photograph. Do you want to pick it up? ")
        choice = input().strip().lower()    
        if choice == "yes":  
            backpack.append ("old photograph ")
            print (backpack)
            time.sleep(2) 
        livingRoom()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(3)
        bedroom()

def searchBackpack(pack, item): 
    #this function should return true if item is inside the list named pack
    found = False 
    for i in range(len(pack)):
        if pack [i] == item:
            found = True 
    return found
    
def openWindow(): 
    slowText ("You decided to try to open the window. ")
    if searchBackpack(backpack, "paper clip") == True:
        slowText ("You used the pap clip to unlock the lock on the window. Now it is open.")
        slowText("You see a wolf in the yard. ")
        if searchBackpack(backpack, "oreas") == True:
            slowText("You use oreos to distract the wolf.")
            slowText("Congratulations you made it out of the house alive." )
        else:
            slowText("You can't evade the wolf right now.")
        time.sleep(3)
        kitchen()
    else: 
        slowText("unfortunately you can't unlock the window.")
        time.sleep(3)
        kitchen()



playerName = ""
backpack = []
start()