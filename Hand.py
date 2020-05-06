class Hand:
    cards = []

    def __init__(self):
        pass


    def set_hand(self, hand):
        self.cards = hand


    def print_hand(self):
        for card in self.cards:
            print("  " + card)
