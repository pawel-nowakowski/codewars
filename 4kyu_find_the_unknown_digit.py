import re


def solve_runes(runes: str) -> int:
    """
    4kyu_find_the_unknown_digit
    :param runes: runes to decypher
    :return: unknown digit
    """
    new_runes = re.split("\+|-|\*|=", runes)
    newer_runes = []
    for i in range(10):
        if str(i) in runes:
            continue
        else:
            for j in range(len(new_runes)):
                if i == 0 and new_runes[j].startswith("?") and len(new_runes[j]) > 1:
                    break
                else:
                    newer_runes.append(new_runes[j].replace("?", str(i)))
            for index in range(len(newer_runes)):
                try:
                    if newer_runes[index] == "":
                        newer_runes[index + 1] = "-" + str(newer_runes[index + 1])
                except IndexError:
                    break
            for index in range(len(newer_runes)):
                try:
                    if newer_runes[index] == "":
                        del newer_runes[index]
                except IndexError:
                    break
            if newer_runes:
                if "+" in runes:
                    try:
                        if int(newer_runes[0]) + int(newer_runes[1]) == int(
                            newer_runes[2]
                        ):
                            return i
                        else:
                            newer_runes = []
                    except IndexError:
                        newer_runes = []
                elif "*" in runes:
                    try:
                        if int(newer_runes[0]) * int(newer_runes[1]) == int(
                            newer_runes[2]
                        ):
                            return i
                        else:
                            newer_runes = []
                    except IndexError:
                        newer_runes = []
                elif "-" in runes:
                    try:
                        if int(newer_runes[0]) - int(newer_runes[1]) == int(
                            newer_runes[2]
                        ):
                            return i
                        else:
                            newer_runes = []
                    except IndexError:
                        newer_runes = []
                else:
                    return -1
    if not newer_runes:
        return -1


print(solve_runes("??+??=??"))
print(solve_runes("2992--?2431=?5423"))
print(solve_runes("?*11=??"))
print(solve_runes("-5?*-1=5?"))
print(solve_runes("76??+144?5=22??5"))
