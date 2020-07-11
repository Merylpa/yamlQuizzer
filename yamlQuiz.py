import yaml
import random
import sys


if len(sys.argv) < 2:
    print("Provide input files for flashcard generation")
    sys.exit(1)

deck = []
for filein in sys.argv[1:]:
    with open(filein) as stream:
        parsed = yaml.load(stream, Loader=yaml.FullLoader)
        deck += parsed

fullDeck = len(deck)
print("\t 'q' to Quit, enter to continue")
userInput = ""
while len(deck) > 0:
    cardsRemaining = len(deck)
    message = str(cardsRemaining) +"/"+ str(fullDeck) +" cards"
    userInput = input(message)
    if userInput == "q":
        break

    randomCard = random.choice(deck)
    print(randomCard['term'])
    defInput = input("\t ....")
    if defInput == "q":
        break
    print(randomCard['definition'])
    deck.remove(randomCard)

