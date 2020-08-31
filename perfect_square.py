from typing import Generator, Iterator


def nats(n: int) -> Generator[int, None, None]:
    yield n
    yield from nats(n+1)


def sieve(s: Iterator[int]) -> Generator[int, None, None]:
    n: int = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


def is_perfect_square(n: int) -> None:
    p: Generator[int, None, None] = sieve(iter(range(2, n)))
    a: int = next(p)
    while a*a <= n:
        print(a)
        a = next(p)


if __name__ == '__main__':
    is_perfect_square(100)
