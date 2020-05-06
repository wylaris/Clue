from Game import ClueGame
import sys

def play_clue(game):
    game.deal()
    game.show_player_cards()
    while True:
        take_guess(game)
        person, weapon, location = game.computer.guess()
        print("\nThe computer guessed it was %s with the %s in the %s" % (person, weapon, location))
        game.computer.remove_from_possible(player_reveal(game, person, weapon, location))


def take_guess(game):
    person = input("Who do you think it was? ")
    if person not in game.people:
        print("Person not found")
        person = input("Who do you think it was? ")

    weapon = input("What do you think they used? ")
    if weapon not in game.weapons:
        print("Weapon not found")
        weapon = input("What do you think they used? ")

    location = input("Where do you think they did it? ")
    if location not in game.locations:
        print("Location not found")
        location = input("Where do you think they did it? ")

    revealed = game.computer.reveal_random_card(person, weapon, location)
    if revealed is not None:
        print("The computer revealed %s" % revealed)
    else:
        print("The computer did not have any of those cards...")
        reveal = input("Do you want to check (Yes, No)? ")
        if reveal == "Yes":
            if game.reveal_secret == (person, weapon, location):
                sys.exit("Congradulations!  You won!")
            else:
                sys.exit("Oh no!  The killer got away...")
        else:
            print("Then we shall continue on...")


def player_reveal(game, person, weapon, location):
    while True:
        card = input("What card do you want to show the computer? ")
        if card in game.player_hand.cards:
            return card
        else:
            print("You do not have that card")


def main():
    game = ClueGame()
    game.initialize()
    play_clue(game)


if __name__ == '__main__':
    main()
