# the following functions are modified from code from Stack Overflow
# CITE: https://stackoverflow.com/questions/1169725/adding-values-from-tuples-of-same-length


def add(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    """
    Adds the values of two tuples together.
    Values in the longer tuple are disregarded.
    """
    if not isinstance(x, tuple) or not isinstance(y, tuple):
        raise TypeError("Parameters must be tuples")
    return tuple(sum(a) for a in zip(x, y))


def subtract(x, y):
    """
    Subtracts the values of two tuples together.
    Values in the longer tuple are disregarded.
    """
    if not isinstance(x, tuple) or not isinstance(y, tuple):
        raise TypeError("Parameters must be tuples")
    return tuple(a - b for a, b in zip(x, y))


def multiply(x, y):
    """
    Multiplies the values of two tuples together.
    Values in the longer tuple are disregarded.
    """
    if not isinstance(x, tuple) or not isinstance(y, tuple):
        raise TypeError("Parameters must be tuples")
    return tuple(a * b for a, b in zip(x, y))


def divide(x, y):
    """
    Divides the values of two tuples together.
    Values in the longer tuple are disregarded.
    """
    if not isinstance(x, tuple) or not isinstance(y, tuple):
        raise TypeError("Parameters must be tuples")
    return tuple(a / b for a, b in zip(x, y))


def do(x, y, op):
    """
    Performs an operation on two tuples.
    Values in the longer tuple are disregarded.
    """
    if not isinstance(x, tuple) or not isinstance(y, tuple):
        raise TypeError("Parameters must be tuples")
    return tuple(op(a, b) for a, b in zip(x, y))
