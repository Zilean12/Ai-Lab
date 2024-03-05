# Constraint Satisfaction Problem (CSP) Solver

---

## 🧩 Overview

Welcome to the Constraint Satisfaction Problem (CSP) Solver lab! In this lab, you will work with a constraint graph for a CSP with unary and binary constraints. The program takes input regarding variables, domains, unary constraints, and binary constraints and performs domain adjustments to satisfy the constraints. This README provides an overview of the lab and instructions for running the program.

## 📝 Input Format

The input consists of the following:

- Total number of variables, N_V
- N_V variable names (single, capital letters like A, B, … Z)
- Domain of each variable (positive integers, finite domain)
- Total number of unary constraints, N_UC
- N_UC constraints written as `<Variable Name> <Relational Operator> <Constant>`
  e.g., A < 5
- Total number of binary constraints, N_BC
- N_BC constraints written as `<Variable Name 1> <Relational Operator> <Variable Name 2> <Arithmetic Operator> <Constant>`
  e.g., X > Y + 5

## ⚙️ Program Functionality

The program performs the following tasks:

1. Reads unary constraints and adjusts the domain of the corresponding variables.
2. Reads binary constraints.
3. Draws a constraint graph with each variable as a node and binary constraints as edges between nodes.
4. Implements logic to adjust domains based on binary constraints. It examines the domain of the variable on the left-hand side and adjusts the domain of the variable on the right-hand side to satisfy the binary constraint (if possible).
5. Redraws the constraint graph with adjusted domains.

## 📌 Instructions

1. Run the program and provide input according to the specified format.
2. Alternatively, you can type input in a text file and read the file as input.
3. Follow the prompts to enter variable names, domains, unary constraints, and binary constraints.
4. View the constraint graph with original domains and adjusted domains.

## 🌟 Example

Consider the following example input:

This input specifies 4 variables (A, B, C, D) with domains (1-5), (1-3), (1-4), and (1-6), respectively. It also contains 2 unary constraints and 3 binary constraints.

## 🎉 Conclusion

This CSP Solver program effectively processes unary and binary constraints, modifies variable domains, and visualizes the constraint graph, providing a useful tool for solving constraint satisfaction problems.

---

*This README provides an overview and instructions for the Constraint Satisfaction Problem (CSP) Solver program, guiding users through usage and example input.* 🧩✨
