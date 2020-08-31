from typing import Generator, Iterator


def nats(n: int) -> Generator[int, None, None]:
    yield n
    yield from nats(n+1)


def sieve(s: Iterator[int]) -> Generator[int, None, None]:
    n: int = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


def prime_numbers(n: int) -> list:
    primes = [2, ]
    for i in range(2, n):
        if all((i % x) != 0 for x in primes):
            primes.append(i)
    return primes


def prime_factors(n: int) -> tuple:
    primes = prime_numbers(n)
    return tuple(x for x in primes if n % x == 0)


def is_perfect_square(n: int) -> None:
    p: Generator[int, None, None] = sieve(iter(range(2, n)))
    a: int = next(p)
    while a*a <= n:
        print(a)
        a = next(p)


if __name__ == '__main__':
    print(prime_numbers(100))
    print(prime_factors(100))
