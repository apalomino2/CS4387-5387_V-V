def split(input, size):
    if size <= 0:
        raise ValueError('Size of %d is negative or zero' % size)
    if input is None:
        raise TypeError('Input %s is null' % input)
    if not input:
        return [""]
    else:
        return [input[start:start+size] for start in range(0, len(input), size)]
