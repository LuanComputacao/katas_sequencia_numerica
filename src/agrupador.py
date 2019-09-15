'''
Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos


'''


def group(numbers):
    conjuntos = find_sequences(numbers)
    conjuntos = [formata(sequence) for sequence in conjuntos]

    return conjuntos


def find_sequences(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return split_sequences(numbers)


def split_sequences(numbers, sequences=[]):
    starts = numbers[0]
    ends, depth = sequence_ends(numbers)
    numbers = numbers[depth+1:]
    sequence = [starts, ends] if ends - starts > 0 else [starts]

    if len(numbers) < 1:
        return sequences + [sequence]
    else:
        return split_sequences(numbers, [sequence])


def sequence_ends(numbers, depth=0):
    if len(numbers) > 1:
        if numbers[1] - numbers[0] != 1:
            return [numbers[0], depth]
        else:
            return sequence_ends(numbers[1:], int(depth + 1))

    return [numbers[0], depth]


def formata(starts_ends):
    len_starts_ends = len(starts_ends)
    if len_starts_ends == 1:
        return "[{}]".format(str(starts_ends[0]))
    elif len_starts_ends == 2:
        return "[{}-{}]".format(str(starts_ends[0]), str(starts_ends[1]))
    else:
        return "[-]"
