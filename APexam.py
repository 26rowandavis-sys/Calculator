def start():
    import os 
    global playerName, locationName, wardrobe
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Welcome to the Clothing Recommender!")
    slowText("Please enter your name: ")
    playerName = input().strip()
    slowText("Hi, {}!".format(playerName))

    slowText("Where do you live (city or region)?")
    locationName = input().strip()

    # Show available clothing
    allClothes = [
        ["Winter Coat", "heavy", True],
        ["Hoodie", "medium", False],
        ["T-shirt", "light", False],
        ["Light Jacket", "medium", True],
        ["Shorts", "light", False],
        ["Scarf", "heavy", False],
        ["Rain Jacket", "medium", True],
        ["Sandals", "light", False],
    ]

    slowText("Here are some clothing items you might own:")
    namesOnly = []
    for item in allClothes:
        namesOnly.append(item[0])
    slowText(", ".join(namesOnly))

    slowText("Type the items you own, separated by commas:")
    ownedText = input()
    ownedPieces = ownedText.split(",")

    # build wardrobe list from user input
    wardrobe = []
    for piece in ownedPieces:
        cleaned = piece.strip().lower()
        for option in allClothes:
            if option[0].lower() == cleaned:
                wardrobe.append(option)

    if len(wardrobe) == 0:
        slowText("You did not match any items, so I will use all items as your wardrobe.")
        wardrobe = allClothes

    slowText("Great! I will recommend outfits for {} in {}.".format(playerName, locationName))
    time.sleep(1.5)
    mainMenu()

def recommendScreen(): 
    import os
    os.system('cls'if os.name == 'nt' else 'clear')

# what user sees
def mainMenu():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    slowText("Clothing Recommender Main Menu")
    slowText("You can: ")
    slowText("- type 'recommend' to get an outfit")
    slowText("- type 'history' to see past weather queries")
    slowText("- type 'quit' to exit")
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

import time
# prints like house game from Mr. James
def slowText(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# helps personalize for user
playerName = ""
locationName = ""
wardrobe = []           

#recommends clothing based on temp, weather and clothes entered, 
def recommendClothing(temp, condition, clothes):
    recommendations = []

    #  over the wardrobe list
    for item in clothes:
        name = item[0]
        warmth = item[1]
        rainSafe = item[2]

        #  based on temperature
        if temp < 40 and warmth == "heavy":
            recommendations.append(name)
        elif 40 <= temp < 70 and warmth == "medium":
            recommendations.append(name)
        elif temp >= 70 and warmth == "light":
            recommendations.append(name)

        # Extra, rainy and rain-safe
        if condition == "rainy" and rainSafe and name not in recommendations:
            recommendations.append(name)

    # Accessories based on weather condition
    if condition == "rainy":
        recommendations.append("Umbrella")
    elif condition == "snowy":
        recommendations.append("Gloves")
    return recommendations


