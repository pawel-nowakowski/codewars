from typing import List


def spiralize(n: int) -> List:
    """
    creates a spiral i.e. with input 5 it will create 5x5 spiral
    :param n: how big spiral must be
    :return: spiral as list
    """
    spiral = []

    for i in range(n):
        spiral.append([])

    for i in range(n):
        spiral[0].append(1)
        spiral[-1].append(1)
        if i == n - 1:
            spiral[1].append(1)
        else:
            spiral[1].append(0)
        if i == n - 1 or i == 0:
            spiral[-2].append(1)
        else:
            spiral[-2].append(0)

    first_half = int(n / 2 + 1)
    second_half = int(n / 2)
    if n % 2 == 0:
        second_half -= 1
    a = 2
    b = 3
    list_a = []
    list_b = [0, n - 1]

    while a < first_half:
        list_a.append(n - a)
        for i in range(n):
            if i in list_a:
                spiral[a].append(0)
            else:
                spiral[a].append(1)
        list_a.append(a - 1)
        a += 2

    while b < first_half:
        list_b.append(n - b)
        for i in range(n):
            if i in list_b:
                spiral[b].append(1)
            else:
                spiral[b].append(0)
        list_b.append(b - 1)
        b += 2

    c = -3
    d = -4
    list_c = []
    list_d = [0, n - 1]
    while c * -1 <= second_half:
        list_c.append((c * -1) - 2)
        list_c.append(n + c + 1)
        for i in range(n):
            if i in list_c:
                spiral[c].append(0)
            else:
                spiral[c].append(1)
        c -= 2

    while d * -1 <= second_half:
        list_d.append((d * -1) - 2)
        list_d.append(n + d + 1)
        for i in range(n):
            if i in list_d:
                spiral[d].append(1)
            else:
                spiral[d].append(0)
        d -= 2

    if n % 4 == 0:
        spiral[int(n / 2)][int((n / 2) - 1)] = 0

    return spiral
