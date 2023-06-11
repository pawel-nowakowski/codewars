from operator import itemgetter


def order_weight(strng):
    strng = strng.split()
    i = 0
    j = 0
    x = 0
    final_list = []
    value_list = []
    while i < len(strng):
        a = sum(map(int, str(strng[i])))
        strng.insert(i + 1, a)
        i += 2
    for i in strng:
        i = int(i)
    while j < len(strng):
        value_list.append(strng[j : j + 2])
        j += 2
    value_list = sorted(value_list, key=itemgetter(1, 0))
    while x < len(value_list):
        final_list.append(value_list[x][0])
        x += 1
    for i in final_list:
        i = str(i)
    strng = " ".join(final_list)
    print(strng)
    return strng


order_weight("11 11")
order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
