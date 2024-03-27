# Agent Program for Exploring and Retrieving the Pot of Gold

## Problem Description

Imagine a square grid of NxN rooms where each room has doors leading to its neighboring rooms (NSEW neighbors only). One room at the edge opens to the outside world, serving as the entry point, and contains a charging station. Another room contains a pot of gold. An agent, powered by a battery with limited charge, must start from the entry point, explore the rooms, locate the pot of gold, and bring it back to the entry point. The agent must decide whether to explore further or return to recharge when its battery is low.

## Instructions

1. Define the environment: Define the NxN rooms with doors, entry point, charging station location, and pot of gold location.

2. Define suitable actions: Define actions the agent can take (e.g., move forward, backward, turn right, turn left) and the conditions under which these actions are performed.

3. Update agent's memory: Keep track of explored rooms and empty rooms in the agent's memory.

4. Output:
   - Print the total time taken (total number of rooms visited).
   - If the agent went to the charging station, print the location of the room where the decision was made.

### Assumptions

1. The agent moves at a constant speed.
2. The agent can sense the pot of gold when it reaches the room containing it.
3. The agent can sense its current location.
4. The time to recharge is zero.


## Conclusion

In this lab, we implemented an agent program for exploring and retrieving the pot of gold in a grid environment with limited battery charge. The agent makes decisions based on its surroundings and updates its memory accordingly.

