from Game import ClueGame

def play_clue(game):
    game.deal()
    game.show_player_cards()
    game.reveal_secret()


def main():
    game = ClueGame()
    game.initialize()
    play_clue(game)


if __name__ == '__main__':
    main()
