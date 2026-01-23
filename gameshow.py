import random
winningDoor = random.randint(1, 3) #picks a random number 1, 3
contestChoice = random.randint(1, 3)

print ("winner: " + str(winningDoor) + "; Contestant Choice: " + str(contestChoice))

revealDoor = random.randint(1, 3) 
while revealDoor == winningDoor or revealDoor == contestChoice:
    revealDoor = random.randint(1, 3)

contestantFinal = random.randint(1, 3)
while contestantFinal == contestChoice or contestantFinal == revealDoor:
    contestantFinal = random.randint(1, 3)

if contestantFinal == winningDoor:
    print("Contestant Wins!")
else:
    print("No winners!")

def trackWinorLose(totalGames):
    wins = 0
    losses = 0
    if winningDoor == contestantFinal: wins += 1
    else: losses -= 1
    for i in range (1, 1000):
        winPercent = wins / totalGames * 100
        print (winPercent)

