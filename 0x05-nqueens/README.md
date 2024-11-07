# 0x05. N Queens

## Overview
This project implements a solution to the N Queens puzzle - the challenge of placing N non-attacking queens on an N×N chessboard.

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- Files should end with a new line
- First line of all files should be exactly `#!/usr/bin/python3`
- Code should use the PEP 8 style (version 1.7.*)
- All files must be executable

## Tasks
### 0. N queens
- Write a program that solves the N queens problem
- Usage: `nqueens N`
    - N must be an integer greater than or equal to 4
- Output: Every possible solution, with one solution per line

## Author
* Joe404
## Algorithm Overview
The solution uses a backtracking algorithm to find all possible arrangements where N queens can be placed on an NxN board without threatening each other. A queen can move horizontally, vertically, and diagonally.

## Implementation Details
- The program validates input arguments
- Uses recursive backtracking to try different queen positions
- Checks for valid positions by ensuring no queen can attack another
- Prints all valid solutions as coordinate pairs

## Example Usage
```bash
./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## File Structure
- `0-nqueens.py`: Main program file containing solution
- `README.md`: Documentation file

## Resources
- [N Queen Problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- [Backtracking Algorithms](https://www.geeksforgeeks.org/backtracking-algorithms/)
