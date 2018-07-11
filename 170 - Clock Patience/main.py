
class Card:
    def __init__(self, value):
        self.value = value
        self.exposed = False


def find_rank(value: str) -> int:
    rank = value[0]

    if rank == 'A':
        return 0
    elif rank == 'T':
        return 9
    elif rank == 'J':
        return 10
    elif rank == 'Q':
        return 11
    elif rank == 'K':
        return 12
    else:
        return int(rank) - 1


def print_pile(piles, position):
    for i in range(len(piles[position])):
        print(piles[position][i].value)


def is_pile_exposed(pile: list) -> bool:
    boolean = True

    for i in range(len(pile)):
        if pile[i].exposed == False:
            boolean = False
            break

    return boolean


def create_piles(deck: list) -> list:
    cards = []

    for i in range(len(deck)):
        for j in range(13):
            cards.append(deck[len(deck) - 1 - i][12 - j])

    piles = []

    for i in range(13):
        piles.append([])

    for i in range(len(cards)):
        position = i % 13
        piles[position].append(Card(cards[i]))

    for i in range(13):
        piles[i] = piles[i][::-1]

    return piles


def play_the_game(deck: list):
    piles = create_piles(deck)

    i = 0
    position = 12

    while True:
        if is_pile_exposed(piles[position]):
            break

        current_card = piles[position].pop(0)
        current_card.exposed = True

        position = find_rank(current_card.value)

        piles[position].append(current_card)

        i += 1

    if i < 10:
        print('0', end = '')

    print(str(i) + ',' + str(current_card.value))


# input = open("input.txt")

while True:
    deck = []

    for i in range(4):
        line = input()
        if line.count('#') != 0:
            # input.close()
            exit()
        deck.append(line.replace('\n', '').split())

    play_the_game(deck)
