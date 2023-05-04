#!/usr/bin/python3
'''
Defines method to execute two operations in this file: Copy All and Paste
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed
    to to result in exactly n H characters
    Args:
        n (int): Integer value for n number of H characters required
        Returns: An integer, if n is impossible to achieve, return 0
    '''

    # It's impossible to get n H chars if n < 1
    if n < 1:
        return 0

    # No operations needed when 1 H char is already gotten, if n = 1
    if n == 1:
        return 0

    # Keeping track of the number of operations using a counter variable
    num_operations = 0

    # Initializing a divisor for n
    n_divisor = 2

    # Looping through all divisors <= sqrt n
    while n_divisor * n_divisor <= n:

        # Increment counter variable if n is divisible by n_divisor
        while n % n_divisor == 0:
            num_operations += n_divisor
            n //= n_divisor
        # Increment n_divisor
        n_divisor += 1

    # If n > 1, meaning there is a prime factor still > sqrt n
    if n > 1:

        # Increment counter variable by adding n to it
        num_operations += n

    # Return  the counter variable
    return num_operations


if __name__ == "__main__":
    n = 9
    print(minOperations(n))
