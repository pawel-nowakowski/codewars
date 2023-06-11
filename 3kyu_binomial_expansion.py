import re
from typing import List


def expand(formula: str) -> str:
    """
    3kyu_binomial_expansion https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b
    :param formula: formula to expand
    :return: expanded formula as str
    """
    expanded_formula = ''
    regex = "\((-?)(\d*)(\D)([+-])(\d*)\)\^(\d+)"
    split = re.findall(regex, formula)[0]
    power = int(split[5])
    if power == 0:
        expanded_formula += '1'
    elif power == 1:
        expanded_formula += f'{split[0]}{split[1]}{split[2]}{split[3]}{split[4]}'
    else:
        middle_of_equation_list = pascal_triangle(power)
        len_list = len(middle_of_equation_list)
        power_one = power
        power_two = 0
        split_1_digit = 1 if split[1] == '' else int(split[1])
        split_4_digit = int(split[4])
        eq_part = 0
        while eq_part < 3:
            if eq_part == 0:
                part_one = '-' if is_odd(power) and split[0] == '-' else ''
                part_two = f'{split_1_digit ** power}'
                if part_two == '1':
                    part_two = ''
                part_three = f'{split[2]}^{power}'
                expanded_formula += part_one + part_two + part_three
                eq_part += 1
            elif eq_part == 2:
                part_n_1 = '-' if is_odd(power) and split[3] == '-' else '+'
                part_n = f'{split_4_digit**power}'
                if part_n == '0':
                    part_n_1, part_n = '', ''
                expanded_formula += part_n_1 + part_n
                eq_part += 1
            elif split[4] == '0':
                eq_part += 1
            else:
                for x in range(len_list):
                    power_one -= 1
                    power_two += 1
                    power_end = '' if power_one == 1 else f'^{power_one}'
                    sign_one = False if is_odd(power_one) and split[0] == '-' else True
                    sign_two = False if is_odd(power_two) and split[3] == '-' else True
                    sign = '+' if not (sign_one ^ sign_two) else '-'
                    expanded_formula += f'{sign}{middle_of_equation_list[x]*(split_1_digit**power_one)*(split_4_digit**power_two)}{split[2]}{power_end}'
                eq_part += 1
    return expanded_formula


def is_odd(number: int) -> bool:
    """
    checks if number is odd
    :param number: number to check
    :return: True if odd, False if even
    """
    return bool(number % 2)


def pascal_triangle(row: int) -> List:
    """
    creates row in pascal triangle (without boundary values)
    :param row: which row to create
    :return: row in pascal triangle without boundary values
    """
    if row in (0, 1):
        return []
    row_1 = [1, 1]
    for row in range(row - 1):
        row_2 = []
        for number in range(row + 1):
            a = row_1[number: number + 2]
            row_2.append(sum(row_1[number: number + 2]))
        row_2.insert(0, 1)
        row_2.append(1)
        row_1 = row_2
    return row_1[1:-1]


print(expand("(x+1)^1"))
print(expand("(x+1)^2"))      # returns "x^2+2x+1"
print(expand("(p-1)^3"))      # returns "p^3-3p^2+3p-1" -> p^3
print(expand("(2f+4)^6"))     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
print(expand("(-2a-4)^0"))    # returns "1"
print(expand("(-12t+43)^2"))  # returns "144t^2-1032t+1849"
print(expand("(r+0)^203"))    # returns "r^203"
print(expand("(-x-1)^2"))     # returns "x^2+2x+1"
print(pascal_triangle(5))