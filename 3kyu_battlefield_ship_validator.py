from typing import List


def validate_battlefield(field: List) -> bool:
    """
    checks if the battlefield for ship game is valid
    :param field: battlefield with ships
    :return: True if field is valid, False if invalid
    """
    ship = [4, 3, 2, 1]
    for v in range(len(field)):
        for h in range(len(field[v])):
            if field[v][h] == 0:
                continue
            elif field[v][h] == 1:
                field[v][h] = 2
                bad_fields = diagonally_bad_fields(v, h)
                vertical_check = vertical_fields(v, h)
                horizontal_check = horizontal_fields(v, h)
                counter = 1
                for bad_field in bad_fields:
                    x, y = bad_field
                    if field[x][y] == 1:
                        return False
                for vertical in vertical_check:
                    x, y = vertical
                    while field[x][y] == 1:
                        field[x][y] = 3
                        for horizontal in horizontal_fields(x, y):
                            a, b = horizontal
                            if field[a][b] == 1:
                                return False
                        for diagonal in diagonally_bad_fields(x, y):
                            a, b = diagonal
                            if field[a][b] == 1:
                                return False
                        counter += 1
                        x += 1
                        if x > 9:
                            break
                for horizontal in horizontal_check:
                    x, y = horizontal
                    while field[x][y] == 1:
                        field[x][y] = 4
                        for vertical in vertical_fields(x, y):
                            a, b = vertical
                            if field[a][b] == 1:
                                return False
                        for diagonal in diagonally_bad_fields(x, y):
                            a, b = diagonal
                            if field[a][b] == 1:
                                return False
                        counter += 1
                        y += 1
                        if y > 9:
                            break
                try:
                    ship[counter - 1] -= 1
                except IndexError:
                    continue

    if ship == [0, 0, 0, 0]:
        return True
    else:
        return False


def validity_check(fields: tuple) -> tuple[int, int]:
    """
    checks if given cords are within the field
    :param fields: tuple of cords to check
    :return: tuple cords (x, y) if within range
    """
    for field in fields:
        x, y = field
        if x in range(10) and y in range(10):
            yield x, y


def vertical_fields(v: int, h: int) -> tuple:
    """
    checks vertical fields
    :param v: vertical cord
    :param h: horizontal cord
    :return: tuple of valid fields that are within the battlefield
    """
    return validity_check(((v + 1, h), (v - 1, h)))


def horizontal_fields(v: int, h: int) -> tuple:
    """
    checks horizontal fields
    :param v: vertical cord
    :param h: horizontal cord
    :return: tuple of valid fields that are within the battlefield
    """
    return validity_check(((v, h - 1), (v, h + 1)))


def diagonally_bad_fields(v: int, h: int) -> tuple:
    """
    checks diagonal fields
    :param v: vertical cord
    :param h: horizontal cord
    :return: tuple of valid diagonal fields that are within the battlefield
    """
    return validity_check(
        ((v + 1, h - 1), (v + 1, h + 1), (v - 1, h - 1), (v - 1, h + 1))
    )


battleField = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

battleField1 = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

battleField2 = [
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
]


if __name__ == "__main__":
    print(validate_battlefield(battleField))
    print(validate_battlefield(battleField1))
    print(validate_battlefield(battleField2))
