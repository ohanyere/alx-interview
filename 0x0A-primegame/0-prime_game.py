#!/usr/bin/python3
'''Determines who wins in a Prime Game'''


def is_prime(n):
    '''Helper function to check if a number is prime'''
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(n):
    '''Helper function to generate a list of prime numbers up to n'''
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes


def play_game(number, primes, is_maria_turn):
    '''Recursive function to simulate the game'''
    if number == 1 or not primes:
        return "Maria" if is_maria_turn else "Ben"

    if is_maria_turn:
        for prime in primes:
            if number % prime == 0:
                updated_primes = [p for p in primes if p != prime]
                result = play_game(number // prime, updated_primes, False)
                if result == "Maria":
                    return "Maria"
        return "Ben"
    else:
        for prime in primes:
            if number % prime == 0:
                updated_primes = [p for p in primes if p != prime]
                result = play_game(number // prime, updated_primes, True)
                if result == "Ben":
                    return "Ben"
        return "Maria"


def isWinner(x, nums):
    '''Main function to determine the winner of each game'''
    maria_wins = 0
    ben_wins = 0

    for n in range(x):
        number = nums[n]
        primes = get_primes(number)
        result = play_game(number, primes, True)

        if result == "Maria":
            maria_wins += 1
        elif result == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
