def missing(s):
    n = 1
    while n < len(s):
        new_list = [s[i:i + n] for i in range(0, len(s), n)]
        a = 0
        for i in range(len(new_list)):
            if str(int(new_list[0]) + i) not in s:
                k = int(new_list[0]) + i
                a += 1
            if a > 1:
                break
        if a == 0:
            return -1
        if a == 1:
            return k
        n += 1
    return -1



print(missing("998999100010011003"))
print(missing("123567"))
print(missing("8990919395"))
print(missing("9899101102"))
print(missing("12357"))
print(missing("599600601602"))
