#!/usr/bin/env python3

from brain_games.game_logic import game_calc
from brain_games import engine


def main():
    engine.run_game(game_calc)


if __name__ == '__main__':
    main()
