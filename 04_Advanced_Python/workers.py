import math

def count_primes(limit):
    """Count the prime numbers below limit. This is slow on purpose (heavy work)."""
    count = 0
    for n in range(2, limit):
        is_prime = True
        for d in range(2, int(math.isqrt(n)) + 1):
            if n % d == 0:
                is_prime = False
                break
        count += is_prime
    return count

def tile_ndvi_stats(args):
    """Make a fake tile of pixels, calculate NDVI and return some statistics."""
    tile_id, size, seed = args
    import random
    rnd = random.Random(seed)
    values = []
    for _ in range(size):
        red = rnd.uniform(0.02, 0.20)
        nir = rnd.uniform(0.05, 0.50)
        values.append((nir - red) / (nir + red))
    vegetation = sum(1 for v in values if v > 0.5)
    return tile_id, round(sum(values) / size, 3), round(vegetation / size * 100, 1)
