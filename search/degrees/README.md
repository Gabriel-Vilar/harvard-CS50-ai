# Degrees

A project developed as part of Harvard's CS50 Introduction to Artificial Intelligence with Python.

## Overview

The goal of this project is to find the shortest connection between two actors based on the movies they have appeared in.

The project represents actors and movies as a graph, using **Breadth-First Search (BFS)** to find the shortest path between two actors.

## My Implementation

The CS50 distribution provided the initial project structure, helper functions, and datasets containing information about actors and movies.

My main task was to implement the `shortest_path` function in `degrees.py`.

I used **Breadth-First Search (BFS)** to explore the graph, keeping track of visited actors and their parent nodes to reconstruct the shortest connection once the target actor was found.

## Concepts Applied

- Graph representation
- Breadth-First Search (BFS)
- Queue-based search
- Visited nodes
- Path reconstruction
- Python data structures

## Dataset

The project includes two datasets provided by CS50:

- `small/`: A smaller dataset for testing.
- `large/`: A larger dataset containing more actors and movies.

## How to Run

From this directory:

```bash
python degrees.py small
```

Or:

```bash
python degrees.py large
```

Follow the terminal instructions to enter the names of two actors.

## Files

- `degrees.py`: Main implementation, including the `shortest_path` function.
- `util.py`: Helper classes and functions provided by CS50.
- `small/`: Small dataset provided by CS50.
- `large/`: Large dataset provided by CS50.