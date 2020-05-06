"""
Main file to play a game of Clue
"""
from Game import ClueGame
import sys


def play_clue(game):
    """Plays the game"""

    computer_playing = True  # By default, the computer is playing
    game.deal()
    game.show_player_cards()
    while True:
        take_guess(game)
        person, weapon, location = game.computer.guess()
        print("\nThe computer guessed it was %s with the %s in the %s" %
              (person, weapon, location))
        player_card = player_reveal(game, person, weapon, location)
        if player_card is not None:  # If the player revealed a card, let the computer know
            game.computer.remove_from_possible(player_card)
        else:
            computer_playing = computer_check(game, person, weapon, location)


def computer_check(game, person, weapon, location):
    """Checks if the computers guess was correct"""

    if game.reveal_secret() == (person, weapon, location):
        sys.exit("Sorry, the computer won but at least we caught the killer!")
    else:
        print("The computer was not correct...")
        return False  # If the computer guesses wrong the player can still continue


def take_guess(game):
    """Has the user take a guess.  If the computer does not reveal a card
       the user can either check against the secret cards or end their turn"""

    person = input("\nWho do you think it was? ").strip()
    while person not in game.people:  # Wait for a valid person
        print("Person not found")
        person = input("Who do you think it was? ").strip()

    weapon = input("What do you think they used? ").strip()
    while weapon not in game.weapons:  # Wait for a valid weapon
        print("Weapon not found")
        weapon = input("What do you think they used? ").strip()

    location = input("Where do you think they did it? ").strip()
    while location not in game.locations:  # Wait for a valid location
        print("Location not found")
        location = input("Where do you think they did it? ").strip()

    revealed = game.computer.reveal_random_card(
        person, weapon, location)  # Checks if the computer has a card
    if revealed is not None:
        print("The computer revealed %s" % revealed)
    else:
        print("The computer did not have any of those cards...")
        reveal = input("Do you want to check (Yes, No)? ")
        if reveal == "Yes":
            if game.reveal_secret() == (person, weapon, location):
                sys.exit("Congradulations!  You won!")  # You win!
            else:
                # You guessed wrong and the game ends
                sys.exit("Oh no!  The killer got away...")
        else:
            print("Then we shall continue on...")


def player_reveal(game, person, weapon, location):
    """Asks the player what card they want to revel to the computer.
       User presses enter to skip the reveal."""

    while True:
        card = input(
            "What card do you want to show the computer? Press enter if you do not have a card to reveal. ").strip()
        if card in game.player_hand.cards:
            return card
        elif card == "":
            return None
        else:
            print("You do not have that card")


def main():
    try:
        game = ClueGame()
        game.initialize()  # Removes the murderer, weapon, and location
        play_clue(game)
    except KeyboardInterrupt:
        sys.exit("\n")
    except Exception as e:
        print("Error: " + str(e))


if __name__ == '__main__':
    main()
