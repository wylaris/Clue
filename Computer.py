from Hand import Hand
import random


class Computer:
    hand = Hand()
    possible_people = []
    possible_weapons = []
    possible_locations = []

    def __init__(self, people, weapons, locations):
        self.possible_people = people
        self.possible_weapons = weapons
        self.possible_locations = locations

    def show_hand(self):
        print("Computer's cards:")
        self.hand.print_hand()

    def add_hand_to_known(self):
        for card in self.hand.cards:
            self.remove_from_possible(card)

    def remove_from_possible(self, card):
        if card in self.possible_people:
            self.possible_people.remove(card)
        elif card in self.possible_weapons:
            self.possible_weapons.remove(card)
        elif card in self.possible_locations:
            self.possible_locations.remove(card)

    def guess(self):
        person = self.possible_people[random.randint(
            0, len(self.possible_people) - 1)]
        weapon = self.possible_weapons[random.randint(
            0, len(self.possible_weapons) - 1)]
        location = self.possible_locations[random.randint(
            0, len(self.possible_locations) - 1)]
        return person, weapon, location

    def reveal_random_card(self, person, weapon, location):
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
