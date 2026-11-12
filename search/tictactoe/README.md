# Tic-Tac-Toe

A project developed as part of Harvard's CS50 Introduction to Artificial Intelligence with Python.

## Status

**In Progress** (Core game logic implemented; AI Minimax and utility evaluation pending).

## Overview

The goal of this project is to implement an AI that plays Tic-Tac-Toe optimally using the Minimax algorithm.

The project represents the game board state and applies adversarial search to determine the best possible move for the player.

## Current Implementation

The CS50 distribution provided the initial project structure, GUI (`runner.py`), and helper functions.

So far, the core rules and state functions in `tictactoe.py` have been implemented:
- `player`: Determines which player's turn it is (X or O).
- `actions`: Returns a set of all possible available actions (empty cells) on the board.
- `result`: Returns the board that results from making a move on the board.
- `winner`: Returns the winner of the game, if there is one.
- `terminal`: Checks if the game is over (won, lost, or tie).

Pending implementation:
- `utility`: Computes the final numerical utility of a terminal board (1, -1, or 0).
- `minimax`: Computes the optimal action for the current player.

## Concepts Applied

- Adversarial Search
- Minimax Algorithm
- Game Theory and State Spaces
- Python data structures and deep copying

## Files

- `tictactoe.py`: Main implementation containing the game logic and pending AI functions.
- `runner.py`: Graphical user interface provided by CS50 to play the game visually.
- `requirements.txt`: List of Python packages required to run the game.
- `OpenSans-Regular.ttf`: Font file used by the graphical interface.