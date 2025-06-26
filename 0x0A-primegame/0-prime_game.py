#!/usr/bin/python3
"""
Prime Game Solution

Maria and Ben play a game with prime numbers.
Given a set of consecutive integers from 1 to n, they take turns
choosing a prime number and removing it and its multiples from the set.
The player who cannot make a move loses.

This module implements the isWinner function to determine the winner
across multiple rounds of the game.
"""


def sieve_of_eratosthenes(max_n):
    """
    Generate all prime numbers up to max_n using Sieve of Eratosthenes.
    
    Args:
        max_n (int): Maximum number to check for primes
        
    Returns:
        list: List of boolean values where index i is True if i is prime
    """
    if max_n < 2:
        return [False] * (max_n + 1)
    
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    
    return is_prime


def count_primes_up_to(n, is_prime):
    """
    Count the number of primes from 2 to n.
    
    Args:
        n (int): Upper limit
        is_prime (list): Boolean array indicating prime numbers
        
    Returns:
        int: Number of primes from 2 to n
    """
    if n < 2:
        return 0
    return sum(is_prime[2:n+1])


def isWinner(x, nums):
    """
    Determine the winner of the prime game across multiple rounds.
    
    The game theory behind this solution:
    - Each prime number removal affects the game state
    - The total number of prime moves determines the winner
    - If the total number of primes is odd, Maria wins (she goes first)
    - If the total number of primes is even, Ben wins
    
    Args:
        x (int): Number of rounds
        nums (list): Array of n values for each round
        
    Returns:
        str or None: "Maria" if Maria wins more rounds, "Ben" if Ben wins more,
                     None if it's a tie or invalid input
    """
    if not nums or x <= 0:
        return None
    
    if x != len(nums):
        return None
    
    # Find the maximum n to optimize prime generation
    max_n = max(nums)
    
    # Generate all primes up to max_n
    is_prime = sieve_of_eratosthenes(max_n)
    
    # Precompute prime counts for all possible n values
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = count_primes_up_to(i, is_prime)
    
    maria_wins = 0
    ben_wins = 0
    
    # Analyze each round
    for n in nums:
        # The winner is determined by the number of prime moves available
        # If odd number of primes, Maria wins (she goes first)
        # If even number of primes, Ben wins
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
