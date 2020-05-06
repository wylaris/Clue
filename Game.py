import random
from Computer import Computer
from Hand import Hand


class ClueGame:
    people = ["Miss Scarlett", "Mr. Green", "Colonel Mustard",
              "Professor Plum", "Mrs. Peakcock", "Dr. Orchid"]
    weapons = ["Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
    locations = ["Kitchen", "Ballroom", "Conservatory", "Dinning Room",
                 "Billiard Room", "Lounge", "Hall", "Study", "Library"]
    secret = []
    player_hand = None
    computer = None
    availabile_cards = None

    def __init__(self):
        self.player_hand = Hand()
        self.availabile_cards = self.people + self.weapons + self.locations

    def initialize(self):
        prand = random.randint(0, len(self.people) - 1)
        wrand = random.randint(0, len(self.weapons) - 1)
        lrand = random.randint(0, len(self.locations) - 1)

        self.secret.append(self.people[prand])
        self.secret.append(self.weapons[wrand])
        self.secret.append(self.locations[lrand])

        self.availabile_cards.remove(self.people[prand])
        self.availabile_cards.remove(self.weapons[wrand])
        self.availabile_cards.remove(self.locations[lrand])
        self.computer = Computer(self.people, self.weapons, self.locations)

    def reveal_secret(self):
        print("Time to figure out who done it!")
        print("It was %s with the %s in the %s" %
              (self.secret[0], self.secret[1], self.secret[2]))
        return (self.secret[0], self.secret[1], self.secret[2])

    def deal(self):
        random.shuffle(self.availabile_cards)
        tempp = []
        tempc = []
        for i in range(0, len(self.availabile_cards), 2):
            tempp.append(self.availabile_cards[i])
        self.player_hand.set_hand(tempp)
        for i in range(1, len(self.availabile_cards), 2):
            tempc.append(self.availabile_cards[i])
        self.computer.hand.set_hand(tempc)
        self.computer.add_hand_to_known()

    def show_player_cards(self):
        print("Player's cards:")
        self.player_hand.print_hand()
