def solution(arg):
    arg.append(0)
    a = 0
    index = 0
    while index < len(arg) - 1:
        while arg[index] + 1 == arg[index + 1]:
            a += 1
            if a == 1:
                range_start = arg[index]
                range_index_start = index
            index += 1
        if a > 1:
            rangeExtracted = f"{range_start}-{range_start + a}"
            arg = (
                arg[0:range_index_start]
                + [rangeExtracted]
                + arg[range_index_start + a + 1 :]
            )
            index = index - a
        index += 1
        a = 0
    del arg[-1]
    arg = map(str, arg)
    final_list = ",".join(arg)
    return final_list


print(
    solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
)
print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
