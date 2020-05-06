import random


class ClueGame:
    people = ["Miss Scarlett", "Mr. Green", "Colonel Mustard",
              "Professor Plum", "Mrs. Peakcock", "Dr. Orchid"]
    weapons = ["Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
    locations = ["Kitchen", "Ballroom", "Conservatory", "Dinning Room",
                 "Billiard Room", "Lounge", "Hall", "Study", "Library"]
    secret = []
    player_hand = None
    computer_hand = None

    def __init__(self):
        self.player_hand = Hand()
        self.computer_hand = Hand()
        pass

    def initialize(self):
        prand = random.randint(0, len(self.people) - 1)
        wrand = random.randint(0, len(self.weapons) - 1)
        lrand = random.randint(0, len(self.locations) - 1)

        self.secret.append(self.people[prand])
        self.secret.append(self.weapons[wrand])
        self.secret.append(self.locations[lrand])

        self.people.pop(prand)
        self.weapons.pop(wrand)
        self.locations.pop(lrand)

    def reveal_secret(self):
        print("Time to figure out who done it!")
        print("It was %s with the %s in the %s" %
              (self.secret[0], self.secret[1], self.secret[2]))


    def deal(self):
        all_cards = self.people + self.weapons + self.locations
        random.shuffle(all_cards)
        tempp = []
        tempc = []
        for i in range(0, len(all_cards), 2):
            tempp.append(all_cards[i])
        self.player_hand.set_hand(tempp)
        for i in range(1, len(all_cards), 2):
            tempc.append(all_cards[i])
        self.computer_hand.set_hand(tempc)


    def show_player_cards(self):
        print("Player's cards:")
        self.player_hand.print_hand()


class Hand:
    cards = []

    def __init__(self):
        pass


    def set_hand(self, hand):
        self.cards = hand


    def print_hand(self):
        for card in self.cards:
            print("  " + card)
