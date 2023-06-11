import re


def expand(formula):
    expanded_formula = ""
    regex = "\((-?)(\d*)(\D)([+-])(\d*)\)\^(\d+)"
    split = re.findall(regex, formula)[0]
    power = int(split[5])
    if power in (0, 1):
        expanded_formula += "1"
    else:
        for i in range(1, power + 1):
            if i == 1:
                part_one = "-" if is_odd(power) and split[0] == "-" else ""
                split_1_digit = 1 if split[1] == "" else int(split[1])
                part_two = f"{split_1_digit ** power}"
                if part_two == "1":
                    part_two = ""
                part_three = f"{split[2]}^{power}"
                expanded_formula += part_one + part_two + part_three
            elif i == power:
                part_n_1 = "-" if is_odd(power) and split[3] == "-" else "+"
                part_n = f"{int(split[4])**power}"
                if part_n == "0":
                    part_n_1, part_n = "", ""
                expanded_formula += part_n_1 + part_n
            else:
                a = power - 1
                # 2ab
                # 3ab^2 + 3a^2b
                # 4a^3b + 4ab^3 + ?
    return expanded_formula


def is_odd(number):
    return bool(number % 2)


def pascal_triangle(row: int):
    if row in (0, 1):
        return []
    row_1 = [1, 1]
    for i in range(row - 1):
        row_2 = []
        row_2.append(sum(row_1[i : i + 2]))
        row_2.insert(0, 1)
        row_2.append(1)
        row_1 = row_2
    return row_1


print(pascal_triangle(2))
print(pascal_triangle(3))

print(expand("(x+1)^2"))  # returns "x^2+2x+1"
print(expand("(p-1)^3"))  # returns "p^3-3p^2+3p-1" -> p^3
print(
    expand("(2f+4)^6")
)  # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
print(expand("(-2a-4)^0"))  # returns "1"
print(expand("(-12t+43)^2"))  # returns "144t^2-1032t+1849"
print(expand("(r+0)^203"))  # returns "r^203"
print(expand("(-x-1)^2"))  # returns "x^2+2x+1"
