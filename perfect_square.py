from typing import Iterator

def nats(n):
    yield n
    yield from nats(n+1)


def sieve(s):
    n: int = next(s)
    yield n
    yield from sieve(i for i in s if i % n != 0)


def is_perfect_square(n):
    p = sieve(iter(range(2,100)))
    a = next(p)
    while a*a <= n:
        print(a)
        a = next(p)

def myfunc():
    p = sieve(nats(2))
    while True:
        print(next(p))

if __name__ == '__main__':
       is_perfect_square(100) 
