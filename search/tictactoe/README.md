# Tic-Tac-Toe

A project developed as part of Harvard's CS50 Introduction to Artificial Intelligence with Python.

## Status

**Completed** (Core game logic, utility evaluation, and Minimax AI fully implemented).

## Overview

The goal of this project is to implement an AI that plays Tic-Tac-Toe optimally using the Minimax algorithm.

The project represents the game board state and applies adversarial search to determine the best possible move for the player, ensuring the AI never loses.

## Implementation Details

The CS50 distribution provided the initial project structure, graphical user interface (`runner.py`), and foundational helper functions.

The following core components were fully implemented in `tictactoe.py`:
- `player`: Determines which player's turn it is (X or O) based on the board state.
- `actions`: Returns a set of all possible available actions (empty cells) on the board.
- `result`: Returns the new board state that results from making a move.
- `winner`: Returns the winner of the game, if there is one.
- `terminal`: Checks if the game is over (won, lost, or tie).
- `utility`: Computes the final numerical utility of a terminal board (1 for X win, -1 for O win, 0 for tie).
- `minimax` (along with `max_value` and `min_value` helper functions): Computes the optimal adversarial action for the current player using recursive game tree search.

## Concepts Applied

- Adversarial Search
- Minimax Algorithm and Recursion
- Game Theory and State Spaces
- Python data structures, list comprehensions, and deep copying

## How to Run

From the `tictactoe` directory (with your virtual environment active):

```bash
python runner.py