# Lab 1: Tic-Tac-Toe Best Move

## Instructions

In this lab, you will be solving a simple problem related to the classic game of tic-tac-toe. Your task is to decide the "best" move for the player with symbol 'x' based on certain rules.

### Problem Description

Recall the tic-tac-toe game where two players take turns marking spaces on a 3x3 grid. The goal is to have three consecutive symbols of the same type in a row, column, or diagonal.

Represent the playing area as a 3x3 matrix, where each element can be blank, 'x', or 'o'. Initially, all matrix elements are blank. As the game progresses, the matrix elements change to either 'x' or 'o'.

### Task

Your task is to determine the best move for the player with symbol 'x'. Use the following rules in order to make the decision:

1. If a row / column / diagonal has two 'x's and the third position is blank, then place the 'x' on the blank.
2. If a row / column / diagonal has two 'o's and the third position is blank, then place the 'x' on the blank.
3. If a row / column / diagonal has one 'x' and the other two positions are blank, then place the 'x' on one of the blanks.
4. If a row / column / diagonal has one 'o' and the other positions are blanks, then place the 'x' on one of the blanks.
5. Place the 'x' on any random blank.

### Conclusion

In this lab, you used your coding skills and common sense to determine the best move for the 'x' player in a tic-tac-toe game. By following specific rules, you were able to make an informed decision on where to place the 'x' symbol.
