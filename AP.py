import os
import time

def slowText(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

playerName = ""
locationName = ""
wardrobe = []

def recommendClothing(temp, condition, clothes):
    recommendations = []
    for item in clothes:
        name = item[0]
        warmth = item[1]
        rainProof = item[2]

        if temp < 40 and warmth == "heavy":
            recommendations.append(name)
        elif 40 <= temp < 65 and warmth == "medium":
            recommendations.append(name)
        elif temp >= 65 and warmth == "light":
            recommendations.append(name)

        if condition == "rainy" and rainProof and name not in recommendations:
            recommendations.append(name)

    if condition == "rainy":
        recommendations.append("Bring Umbrella with raincoat, and boot ")
    elif condition == "snowy":
        recommendations.append("Make sure to wear Gloves along with a heavy jacket ")
    return recommendations

def recommendScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("You are looking for some clothing recommendations! Tell me the weather and I can help you out.")

    slowText("What is the temperature in degrees (F)?")
    temp = int(input().strip())

    slowText("What is the weather like? (sunny, rainy, snowy)")
    condition = input().strip().lower()

    outfits = recommendClothing(temp, condition, wardrobe)
    slowText("Here is what I recommend you wear:")
    slowText(", ".join(outfits))

    slowText("Press Enter to go back to the main menu.")
    input()
    mainMenu()

def mainMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Clothing Recommender Main Menu")
    slowText("You can: ")
    slowText(" type 'recommend' to get an outfit")
    slowText(" type 'history' to see past weather queries")
    slowText(" type 'quit' to exit")
    choice = input().strip().lower()

    if choice == "recommend":
        recommendScreen()
    elif choice == "quit":
        slowText("Goodbye!")
        time.sleep(1)
    else:
        slowText("Invalid choice. Please try again.")
        time.sleep(2)
        mainMenu()

def start():
    global playerName, locationName, wardrobe

    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Welcome to the Clothing Recommender!")
    slowText("Please enter your name: ")
    playerName = input().strip()
    slowText("Hi, {}!".format(playerName))

    slowText("Where do you live (city or region)?")
    locationName = input().strip()

    allClothes = [
         ["Winter Coat", "heavy", True], ["Hoodie", "medium", False], ["T-shirt", "light", False], ["Light Jacket", "medium", True], ["Shorts", "light", False],
        ["Scarf", "heavy", False],
        ["Rain Jacket", "medium", True],
        ["Sandals", "light", False],
        ["Baseball Cap", "light", False],
        ["Rainboots", "medium", True]
        ]

    slowText("Here are some basic clothing items you might own:")
    namesOnly = [item[0] for item in allClothes]
    slowText(", ".join(namesOnly))

    slowText("Type the items you own, separated by commas:")
    ownedText = input()
    ownedPieces = ownedText.split(",")

    wardrobe = []
    for piece in ownedPieces:
        cleaned = piece.strip().lower()
        for option in allClothes:
            if option[0].lower() == cleaned:
                wardrobe.append(option)

    if len(wardrobe) == 0:
        slowText("You did not match any items, so I will use the whole pre-loaded list as your wardrobe.")
        wardrobe = allClothes

    slowText("Great! I will recommend outfits for {} in {}.".format(playerName, locationName))
    time.sleep(1.5)
    mainMenu()

if __name__ == "__main__":
    start()
