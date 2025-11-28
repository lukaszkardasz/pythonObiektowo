#Higher or lower

import random

#Stałe przedstawiające karty
SUIT_TUPLE = ('pik', 'karo', 'trefl', 'kier')
RANK_TUPLE = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'walet', 'dama', 'król')

NCARDS = 8

def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

print(f"Witaj w grze Większa lub mniejsza!\nZasady są proste. Musisz odgadnąć, czy kolejna karta będzie większa czy mniejsza od poprzedniej.\nJeżeli zgadniesz, zdobywasz 20 punktów. W przeciwnym razie tracisz 15 punktów.\n Na począek masz 50 punktów. \n")
startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50
while True:
    print()
    gameDeckList = shuffle(startingDeckList.copy())
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardSuit = currentCardDict['suit']
    currentCardValue = currentCardDict['value']
    print(f"Twoja pierwsza karta to {currentCardRank} {currentCardSuit}.\n")

    correct = 0
    incorrect = 0

    for cardNumber in range(0, NCARDS):
        if not gameDeckList:
            print("Brak wystarczającej liczby kart w talii. Runda zakończona.")
            break
        prompt = (
            f"Czy następna karta będzie większa czy mniejsza niż {currentCardRank} {currentCardSuit}?\n"
            "Wpisz:\n"
            "  'w' dla większa\n"
            "  'm' dla mniejsza\n"
            "  'q' aby zakończyć\n"
        )
        answer = input(prompt)
        answer = answer.casefold()
        if answer == 'q':
            print("Koniec gry. Twój końcowy wynik to:", score)
            exit()
        if not gameDeckList:
            print("Brak wystarczającej liczby kart w talii. Runda zakończona.")
            break
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print(f"Następna karta to {nextCardRank} {nextCardSuit}.")

        if answer == 'w':
            if nextCardValue > currentCardValue:
                score += 20
                correct += 1
                print("Dobra robota! Zdobywasz 20 punktów.")
            else:
                score -= 15
                incorrect += 1
                print("Niestety, tracisz 15 punktów.")

        elif answer == 'm':
            if nextCardValue < currentCardValue:
                score += 20
                correct += 1
                print("Dobra robota! Zdobywasz 20 punktów.")
            else:
                score -= 15
                incorrect += 1
                print("Niestety, tracisz 15 punktów.")

        else:
            print("Nieprawidłowy wybór, pomijam rundę.")

        currentCardRank = nextCardRank
        currentCardSuit = nextCardSuit
        currentCardValue = nextCardValue

    # Podsumowanie rundy
    print("\n--- Podsumowanie rundy ---")
    print(f"Prawidłowe odpowiedzi: {correct}")
    print(f"Nieprawidłowe odpowiedzi: {incorrect}")
    print(f"Twój aktualny wynik: {score}")

    cont = input("Naciśnij Enter, aby zagrać kolejną rundę lub 'q', aby zakończyć.\n").casefold()
    if cont == 'q':
        print("Koniec gry. Twój końcowy wynik to:", score)
        break
