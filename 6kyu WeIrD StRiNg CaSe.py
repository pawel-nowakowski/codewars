def to_weird_case(string):
    string = list(string)
    k = 0
    for i in range(len(string)):
        if string[i] == " ":
            k = -1
            i += 1
        if k % 2 == 0:
            string[i] = string[i].upper()
        k += 1
    string = "".join(string)
    return string


to_weird_case("This is a test")
