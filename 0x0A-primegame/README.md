# 0x0A. Prime Game

## Description
This project implements a solution to the Prime Game problem where Maria and Ben play optimally in a game involving prime numbers.

## Game Rules
- Given a set of consecutive integers from 1 to n
- Players take turns choosing a prime number and removing it along with all its multiples
- The player who cannot make a move loses
- Maria always goes first
- Both players play optimally

## Problem
Determine the winner across multiple rounds of the game.

## Requirements
- Python 3.4.3 on Ubuntu 20.04 LTS
- PEP 8 style compliance
- No external packages allowed
- All files must be executable
- Files must end with newline
- First line must be `#!/usr/bin/python3`

## Files
- `0-prime_game.py`: Main implementation of the isWinner function
- `main_0.py`: Test file provided for validation
- `README.md`: This documentation file

## Algorithm Approach
The solution uses:
1. Sieve of Eratosthenes to efficiently find all primes up to the maximum n
2. Game theory analysis to determine winners based on the number of prime moves available
3. Optimization through precomputation and memoization

## Usage
```bash
./main_0.py
```

## Example
For x=3, nums=[4, 5, 1]:
- Round 1 (n=4): Ben wins
- Round 2 (n=5): Maria wins  
- Round 3 (n=1): Ben wins
- Result: Ben wins overall (2 wins vs 1 win)

## Author
Solution implemented following ALX project requirements.
