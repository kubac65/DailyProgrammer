def warmup1(input_data):
    """
    Removes zeros from the list
    """
    return [i for i in input_data if i != 0]

def warmup2(input_data):
    """
    Sorts list in descending order
    """
    return sorted(input_data, reverse=True)

def warmup3(n, seq):
    """
    Checks whethere number n is greater than sequence length
    """
    return n > len(seq)

def warmup4(n, seq):
    """
    Subracts 1 from first n elements of the sequence
    """
    return [i-1 for i in seq[: n]] + [i for i in seq[n:]]

def hh(seq):
    breakpoint
    seq = warmup1(seq)
    if len(seq) == 0:
        return True

    seq = warmup2(seq)
    n = seq[0]
    seq = seq[1:]

    if warmup3(n, seq):
        return False

    seq = warmup4(n, seq)
    return hh(seq)