# Smart Elevator

Intelligent Elevator Control System, an AI course project.

We simulate elevators in a building and compare different ways of
choosing which way a lift should move.

## Current status

- One lift in a 8-floor building.
- Controllers: FCFS, nearest-request and LOOK.
- Search model (states, transitions) started in `search_problem.py`.
- Multi-lift control, BFS/DFS/A*, MDP and Q-learning are not built yet.

## How to run

From inside this folder:

    python main.py

## Design notes

### Search ignores dwell time

The simulator adds a dwell time (door open and passenger boarding)
at every stop. The search model in `search_problem.py` does not.
There, a move is just one floor up, down, or a stay, and boarding
happens as soon as the lift arrives.

This is a deliberate abstraction. Search is only used on small cases
as an offline benchmark, to get optimal baselines. The full
simulation, with dwell time, is used to compare the dispatchers.
Search results are therefore compared by path cost, not by exact
simulation time.
