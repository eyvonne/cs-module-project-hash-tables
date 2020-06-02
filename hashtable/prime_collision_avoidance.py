import math
import numpy as np
'''this code was written thinking I could build a 2-d hash table that is
less likely to experience collision. I think it still makes sense that this would
experience collisions slower than a 1-d of the same capacity once it was filled that
wouldn't really make a difference, ultimatelly leading to a lot of work for very
little difference in performance'''


def get_primes(max):
    count = 2
    primes = []
    while count < max:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            primes.append(count)

        count += 1
    return primes


def generate_multiplication_table(numbers):
    table = np.full((len(numbers), len(numbers)), None)
    for h, i in enumerate(numbers):
        for k, j in enumerate(numbers):
            table[h][k] = i * j
    return table, numbers


if __name__ == '__main__':
    CAPACITY = 10
    primes = get_primes(CAPACITY)
    print(generate_multiplication_table(primes))
