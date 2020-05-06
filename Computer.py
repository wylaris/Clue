"""
Computer class
"""

from Hand import Hand
import random


class Computer:
    hand = Hand()
    possible_people = []
    possible_weapons = []
    possible_locations = []

    def __init__(self, people, weapons, locations):
        """Creates a new computer with the all the possible cards (still
           includes the ones removed)"""

        self.possible_people = people.copy()  # Copy so it doesn't edit the official one
        self.possible_weapons = weapons.copy()
        self.possible_locations = locations.copy()

    def show_hand(self):
        """Prints out the computer's cards, not meant to be used in the game"""

        print("Computer's cards:")
        self.hand.print_hand()

    def remove_hand_from_possible(self):
        """Removes the cards in the computers hand from the possible cards left"""

        for card in self.hand.cards:
            self.remove_from_possible(card)

    def remove_from_possible(self, card):
        """Removes the given card from the possible cards left"""

        if card in self.possible_people:
            self.possible_people.remove(card)
        elif card in self.possible_weapons:
            self.possible_weapons.remove(card)
        elif card in self.possible_locations:
            self.possible_locations.remove(card)

    def guess(self):
        """Takes a guess at the secret by randomly guessing from the possible
           cards remaining"""

        person = self.possible_people[random.randint(
            0, len(self.possible_people) - 1)]
        weapon = self.possible_weapons[random.randint(
            0, len(self.possible_weapons) - 1)]
        location = self.possible_locations[random.randint(
            0, len(self.possible_locations) - 1)]
        return person, weapon, location

    def reveal_random_card(self, person, weapon, location):
        """Takes in the cards the user guessed and randomly reveals one if possible"""

        can_reval = []
        if person in self.hand.cards:
            can_reval.append(person)
        if weapon in self.hand.cards:
            can_reval.append(weapon)
        if location in self.hand.cards:
            can_reval.append(location)

        if len(can_reval) == 1:
            return can_reval[0]
        elif len(can_reval) > 1:
            return can_reval[random.randint(0, len(can_reval) - 1)]
        else:
            return None
