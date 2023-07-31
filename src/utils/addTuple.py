# CITE: https://stackoverflow.com/questions/1169725/adding-values-from-tuples-of-same-length
def add(t1, t2):
    """
    Adds the values of two tuples together.
    They must be of the same length.
    """
    return tuple(sum(x) for x in zip(t1, t2))
