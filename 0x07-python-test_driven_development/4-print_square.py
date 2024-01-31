#!/usr/bin/python3
"""Module for text_indentation method."""


def print_square(size):
    """Method for printing a square with # characters.

    Args:
        size: The int size of the aquare's side.

    Raises:
        TypeError: If size is not an int.
        ValueError: if size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("sizemust be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
