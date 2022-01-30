import itertools
def permutations(string):
    string = list(string)
    length = len(string)
    final_combinations = []
    combination_list = list(itertools.permutations(string, length))
    combination_list = set(combination_list)
    for i in combination_list:
        final_combinations.append(''.join(i))
    return final_combinations