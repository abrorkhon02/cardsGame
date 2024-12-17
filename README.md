# Cards Game

A Python-based multiplayer card game where players compete using colored number cards.

## Features

- Player count: 2-4 players
- Card deck: Numbers 1-13 in four colors (GREEN, YELLOW, BLUE, RED)
- Special ace card mechanic for enhanced gameplay
- Point-based scoring system
- Interactive command-line interface

## Game Rules

- Players receive equal number of cards at start
- One card is randomly selected as the "ace card" color (trump)
- Each round, players take turns playing one card
- Winning conditions:
  - Ace color cards beat all other colors
  - Between ace color cards, higher number wins
  - Between non-ace colors, higher number wins
  - Equal cards result in a tie
  - Points accumulate over multiple rounds

## Project Structure

- [`main.py`](main.py): Main game loop and orchestration
- [`card_create.py`](card_create.py): Card deck creation and shuffling
- [`card_distribute.py`](card_distribute.py): Card dealing functionality
- [`card_compare.py`](card_compare.py): Card comparison logic

## Setup & Usage

1. Requirements:
   Python 3.x
2. ```bash
   python main.py
   ```
3. Gameplay flow:
   - Enter number of players (2-4)
   - Each Round:
     - View your cards
     - Select card by index
     - See round results
   - Final scores displayed at the end
   - Option to play again
