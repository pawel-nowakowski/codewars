from math import factorial
def listPosition(word):
    word_list = list(word)
    sorted_list = list(word)
    sorted_list.sort()
    rank = 1
    a = {i: word_list.count(i) for i in word_list if word_list.count(i) > 1}
    b = [word_list.count(i) for i in set(word_list) if word_list.count(i) > 1]
    c = 1
    for index in b:
        c *= factorial(index)
    print(a)
    print(b)
    print(sorted_list)
    for letter in word_list:
        n = sorted_list.index(letter)
        sorted_list.remove(letter)
        v = len(sorted_list)
        rank += n*(int(factorial(v)/c))
        if letter in a:
            c = c/a[letter]
            a[letter] -= 1
    return rank