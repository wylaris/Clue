from Game import ClueGame

def play_clue(game):
    game.deal()
    game.show_player_cards()
    take_guess(game)
    person, weapon, location = game.computer.guess()
    print("The computer guessed it was %s with the %s in the %s" % (person, weapon, location))
    game.reveal_secret()


def take_guess(game):
    person = input("Who do you think it was? ")
    weapon = input("What do you think they used? ")
    location = input("Where do you think they did it? ")

    revealed = game.computer.reveal_random_card(person, weapon, location)
    if revealed is not None:
        print("The computer revealed %s" % revealed)
    else:
        print("The computer did not have any of those cards...")
        reveal = input("Do you want to check (Yes, No)? ")

def main():
    game = ClueGame()
    game.initialize()
    play_clue(game)


if __name__ == '__main__':
    main()
