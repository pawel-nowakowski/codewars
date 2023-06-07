def count_patterns_from(firstPoint, length, possibilities=0, a=0, exclude=None):
    if exclude is None:
        exclude = []
    if len(exclude) != 5 - length:
        exclude = exclude[:5 - length]
    patterns = {
        'A': ['B', 'D', 'E', 'F', 'H'],
        'B': ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
        'C': ['B', 'D', 'E', 'F', 'H'],
        'D': ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
        'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'],
        'F': ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
        'G': ['B', 'D', 'E', 'F', 'H'],
        'H': ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
        'I': ['B', 'D', 'E', 'F', 'H'],
    }
    if length == 2:
        reduce = 0
        for letter in exclude:
            if letter in patterns[firstPoint]:
                reduce += 1
        b = len(patterns[firstPoint]) - reduce
        return b
    elif length == 0 or length > 9:
        return 0
    elif length == 1:
        return 1
    exclude.append(firstPoint)
    for letter in patterns[firstPoint]:
        a += count_patterns_from(letter, length - 1, possibilities, a, exclude)
    possibilities += a
    return possibilities


print(count_patterns_from('E', 4))
print(count_patterns_from('E', 3))
print(count_patterns_from('A', 3))
print(count_patterns_from('F', 3))
"""
print(count_patterns_from('A', 10) == 0)
print(count_patterns_from('A', 0) == 0)
print(count_patterns_from('E', 14) == 0)
print(count_patterns_from('B', 1) == 1)
print(count_patterns_from('C', 2) == 5)
print(count_patterns_from('E', 2) == 8)
print(count_patterns_from('C', 2) == 5)
print(count_patterns_from('E', 4) == 256)"""