#!/usr/bin/env python3

from brain_games.game_logic import game_even
from brain_games import engine


def main():
    engine.run_game(game_even)


if __name__ == '__main__':
    main()
