"""
Hand class
"""


class Hand:
    cards = []

    def __init__(self):
        pass

    def set_hand(self, hand):
        """Sets the hand to the given list"""
        self.cards = hand

    def print_hand(self):
        """Prints all the cards in the hand"""
        for card in self.cards:
            print("  " + card)
