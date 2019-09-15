#
"""
Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos

"""


def group(numbers):
    """ Group the number sequences
    :param numbers: 
    :return: 
    """
    groups = find_sequences(numbers)
    groups = [sequence_to_string(sequence) for sequence in groups]

    return groups


def find_sequences(numbers):
    """Sort the sequence and returns the splited sequence
    
    :param numbers: numbers list
    :return: list of sequences
    """
    numbers = list(set(numbers))
    numbers.sort()

    return group_sequences(numbers)


def group_sequences(numbers, sequences=[]):
    """Group a numbers list into sequence representations
    
    :param numbers: 
    :param sequences: list of numbers list of sequence representation
    :return: 
    """
    starts = numbers[0]
    ends, depth = sequence_ends(numbers)

    numbers = numbers[depth + 1:]
    sequence = [starts, ends] if ends - starts > 0 else [starts]

    new_sequences = sequences + [sequence]

    if len(numbers) < 1:
        return new_sequences
    else:
        return group_sequences(numbers, new_sequences)


def sequence_ends(numbers, depth=0):
    """Find the last number of a sequence of the first number
    
    :param numbers: numbers list
    :type numbers: list
    :param depth: amount of numbers forwarded
    :type depth: int
    :return: The number and the forwarded steps to the last number of the sequence
    :rtype list:
    """
    if len(numbers) > 1:
        if numbers[1] - numbers[0] != 1:
            return [numbers[0], depth]
        else:
            return sequence_ends(numbers[1:], int(depth + 1))

    return [numbers[0], depth]


def sequence_to_string(starts_ends):
    """Convert the sequence list representation to a sequence string representation
    
    :param starts_ends: 
    :return: 
    """
    len_starts_ends = len(starts_ends)
    if len_starts_ends == 1:
        return "[{}]".format(str(starts_ends[0]))
    elif len_starts_ends == 2:
        return "[{}-{}]".format(str(starts_ends[0]), str(starts_ends[1]))
    else:
        return "[-]"
