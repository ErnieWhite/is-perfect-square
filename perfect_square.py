from math import sqrt
from typing import Generator, Iterator


def is_perfect_square(n: int) -> bool:
    return sqrt(n).is_integer()


if __name__ == '__main__':
    print(is_perfect_square(4))
