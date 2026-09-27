import math

def count_primes(limit):
    """count primes below limit (deliberately slow, CPU bound)"""
    count = 0
    for n in range(2, limit):
        is_p = True
        for d in range(2, int(math.isqrt(n)) + 1):
            if n % d == 0:
                is_p = False
                break
        count += is_p
    return count

def square(x):
    return x * x

def district_stats(item):
    name, values = item
    return name, round(sum(values) / len(values), 1), max(values)
