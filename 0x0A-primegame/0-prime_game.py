#!/usr/bin/python3
"""Eratosthenes algorithm for game winner determination"""


def isWinner(x, nums):
    """Determine the winner using the Eratosthenes prime sieving algorithm"""
    Ben = 0
    Maria = 0

    for round in range(x):
        playing_numbers = [num for num in range(2, nums[round] + 1)]
        i = 0  # Renamed 'index' to 'i' for brevity

        while i < len(playing_numbers):
            current_prime = playing_numbers[i]
            multiple_index = (
                i + current_prime
            )  # Renamed 'sieve_index' to 'multiple_index'

            while multiple_index < len(playing_numbers):
                playing_numbers.pop(multiple_index)
                multiple_index += current_prime - 1

            i += 1

        prime_count = len(playing_numbers)
        if prime_count and prime_count % 2:
            Maria += 1
        else:
            Ben += 1

    if Ben == Maria:
        return None
    return "Ben" if Ben > Maria else "Maria"
