from Game import ClueGame
import sys


def play_clue(game):
    computer_playing = True
    game.deal()
    game.show_player_cards()
    while True:
        take_guess(game)
        person, weapon, location = game.computer.guess()
        print("\nThe computer guessed it was %s with the %s in the %s" %
              (person, weapon, location))
        player_card = player_reveal(game, person, weapon, location)
        if player_card is not None:
            game.computer.remove_from_possible(player_card)
        else:
            computer_playing = computer_check(game, person, weapon, location)


def computer_check(game, person, weapon, location):
    if game.reveal_secret() == (person, weapon, location):
        sys.exit("Sorry, the computer won but at least we caught the killer!")
    else:
        print("The computer was not correct...")
        return False


def take_guess(game):
    person = input("\nWho do you think it was? ").strip()
    while person not in game.people:
        print("Person not found")
        person = input("Who do you think it was? ").strip()

    weapon = input("What do you think they used? ").strip()
    while weapon not in game.weapons:
        print("Weapon not found")
        weapon = input("What do you think they used? ").strip()

    location = input("Where do you think they did it? ").strip()
    while location not in game.locations:
        print("Location not found")
        location = input("Where do you think they did it? ").strip()

    revealed = game.computer.reveal_random_card(person, weapon, location)
    if revealed is not None:
        print("The computer revealed %s" % revealed)
    else:
        print("The computer did not have any of those cards...")
        reveal = input("Do you want to check (Yes, No)? ")
        if reveal == "Yes":
            if game.reveal_secret() == (person, weapon, location):
                sys.exit("Congradulations!  You won!")
            else:
                sys.exit("Oh no!  The killer got away...")
        else:
            print("Then we shall continue on...")


def player_reveal(game, person, weapon, location):
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
        game.initialize()
        play_clue(game)
    except KeyboardInterrupt:
        sys.exit("\n")
    except Exception as e:
        print("Error: " + str(e))


if __name__ == '__main__':
    main()
