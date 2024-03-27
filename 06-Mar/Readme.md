# Lab 7: MINMAX Principle and Alpha-Beta Pruning

## Instructions

In today’s lab, you will build the complete solution for using the MINMAX principle to arbitrary game trees and then improve it using alpha-beta pruning. Follow the steps below:

### Step-by-Step Guide

1. **Generate Arbitrary Game Tree**: Start from a root node and generate an arbitrary game tree of depth ‘d’. For each node, generate 3 to 5 children. Assign random numbers (in the range -5 to +5) as utility values for the leaf nodes.

2. **Apply MINMAX Principle**: Assuming that the root node is a MAX node, apply the MINMAX principle to find the best choice.

3. **Count Nodes Visited**: Note the number of nodes visited during the application of the MINMAX principle (essentially all nodes in this case).

4. **Incorporate Alpha-Beta Pruning**: Modify the MINMAX code to incorporate alpha-beta pruning.

5. **Check Optimal Solution**: Check if the same optimal solution is generated after incorporating alpha-beta pruning.

6. **Count Nodes Visited with Pruning**: Note the number of nodes visited after applying alpha-beta pruning.

### Additional Notes

- Ensure to implement the MINMAX algorithm and alpha-beta pruning correctly.
- Keep track of the number of nodes visited to analyze the efficiency of the algorithms.

## Conclusion

In this lab, you learned about the MINMAX principle and alpha-beta pruning in the context of game trees. By implementing and comparing both approaches, you gained insights into their effectiveness in finding optimal solutions while minimizing the number of nodes visited.
