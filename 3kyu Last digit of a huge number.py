zero_dict = {
"0": 1,
"1": 1,
"2": 16,
"3": 1,
"4": 16,
"5": 5,
"6": 6,
"7": 1,
"8": 16,
"9": 1,
}

def last_digit(numbers):
    last_dig = 1
    single_dig = True
    length_of_list = len(numbers) - 1
    if length_of_list == 0:
        return int(str(numbers[0])[-1])
    for i in range(length_of_list)[::-1]:
        if i == length_of_list:
            continue
        if i == length_of_list - 1:
            first_num = numbers[i]
            if len(str(first_num)) > 1:
                single_dig = False
            first_num = int(str(first_num)[-2:]) % 100
            next_num = numbers[i + 1]
            next_num = int(str(next_num)[-2:]) % 100
            last_dig = first_num ** next_num
        else:
            next_num = numbers[i]
            next_num = int(str(next_num)[-2:]) % 100
            if last_dig == 0 and single_dig == False:
                last_dig = zero_dict[str(next_num)[-1]]
            elif last_dig == 1 and int(str(next_num)[-1]) == 2 and single_dig == False:
                last_dig = 12
            last_dig = next_num ** last_dig
        if len(str(next_num)) > 1:
            single_dig = False
        last_dig = last_dig % 100
    last_dig = int(str(last_dig)[-1])
    return last_dig
print(last_digit([2, 2, 2, 0])) #4
print(last_digit([12, 30, 21])) #6
print(last_digit([2, 0, 1])) #1
print(last_digit([2, 2, 101, 2])) #6
