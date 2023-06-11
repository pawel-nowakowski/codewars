def parts_sums(ls):
    i = -2
    j = -(len(ls)) - 1
    ls.append(0)
    while i >= j:
        ls[i] += ls[i + 1]
        i -= 1
    print(ls)


parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358])
