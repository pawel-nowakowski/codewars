def high_and_low(numbers):
    numbers = numbers.split()
    print(numbers)
    high = int(numbers[0])
    low = int(numbers[0])
    for i in numbers:
        i = int(i)
        if i > high:
            high = i
        if i < low:
            low = i
    high_low_list = []
    high_low_list.append(str(high))
    high_low_list.append(str(low))
    high_low_list = ' '.join(high_low_list)
    print(high_low_list)
    return high_low_list
high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")