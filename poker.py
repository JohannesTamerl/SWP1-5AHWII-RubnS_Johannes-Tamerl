import random
import matplotlib.pyplot as plt


# Fraben
colors = 4

# Symbole
symbols = 13

# Karten die gezogen werden
hand = 5


def create_cards():
    return [i for i in range(colors * symbols)]


def get_hand(numberofcards):
    deck = create_cards()
    random.shuffle(deck)
    return deck[:numberofcards]


def get_color(card):
    return card // symbols


def get_symbol(card):
    return card % symbols


def check_values(cards):
    emptylist = [0] * symbols
    # Gehe meine Karten durch und erhöhe in der Leste an der jeweiligen Symbolstelle um 1,
    # somit weiß ich schlußendlich wieviel ich von den jeweiligen Symbolen in meiner Hand halte
    for card in cards:
        emptylist[get_symbol(card)] += 1
    return emptylist


def pair(cards):
    emptylist = check_values(cards)
    # Zwei Karten von gleichem Wert
    return 2 in emptylist


def two_pairs(cards):
    emptylist = check_values(cards)
    # Hier muss man zusätzlich überprüfen, ob ich zwei Paare in der Hand halte
    return emptylist.count(2) == 2

def drilling(cards):
    emptylist = check_values(cards)
    # Drei Karten von gleichem Wert
    return 3 in emptylist


def straight(cards):
    values = [get_symbol(card) for card in cards]
    values.sort()
    for i in range(0, 4):
        if values[i] != values[i + 1] - 1:
            return False
    return True


def flush(cards):
    all_colors = [get_color(card) for card in cards]
    all_colors.sort()
    return all_colors[0] == all_colors[4]


def full_house(cards):
    return drilling(cards) and pair(cards)

def vierling(cards):
    emptylist = check_values(cards)
    return 4 in emptylist


def straight_flush(cards):
    return flush(cards) and straight(cards)


def royal_flush(cards):
    values = [get_symbol(card) for card in cards]
    values.sort()
    symbols = [8, 9, 10, 11, 12]
    return values == symbols


def highest_card(cards):
    if pair(cards) or two_pairs(cards) or drilling(cards) or straight(cards) or flush(cards) or full_house(
            cards) or vierling(cards) \
            or straight_flush(cards) or royal_flush(cards):
        return False
    return True


def check(cards, combinations):

    if royal_flush(cards):
        combinations["royal_flush"] += 1
        return
    elif straight_flush(cards):
        combinations["straight_flush"] += 1
        return
    elif vierling(cards):
        combinations["vierling"] += 1
        return
    elif full_house(cards):
        combinations["full_house"] += 1
        return
    elif flush(cards):
        combinations["flush"] += 1
        return
    elif straight(cards):
        combinations["straight"] += 1
        return
    elif drilling(cards):
        combinations["drilling"] += 1
        return
    elif two_pairs(cards):
        combinations["two_pairs"] += 1
        return
    elif pair(cards):
        combinations["pair"] += 1
        return
    else:
        combinations["high_card"] += 1


def simulation(durchgaenge):
    combinations = {
        "high_card": 0,
        "pair": 0,
        "two_pairs": 0,
        "drilling": 0,
        "straight": 0,
        "flush": 0,
        "full_house": 0,
        "vierling": 0,
        "straight_flush": 0,
        "royal_flush": 0
    }

    wahrscheinlichkeit = {
        "high_card": 0,
        "pair": 0,
        "two_pairs": 0,
        "drilling": 0,
        "straight": 0,
        "flush": 0,
        "full_house": 0,
        "vierling": 0,
        "straight_flush": 0,
        "royal_flush": 0
    }

    for i in range(durchgaenge):
        check(get_hand(5), combinations)

    for x in combinations:
        wahrscheinlichkeit[x] = (combinations[x] / durchgaenge) * 100

    return wahrscheinlichkeit
    print(combinations)
    print(wahrscheinlichkeit)
list = simulation(10000)
print(list.values())
print(list.keys())
plt.pie(list.values(), labels=list.keys())
plt.show()
