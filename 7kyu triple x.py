def triple_x(s):
    s = list(s)
    if "x" not in s:
        return False
    for i in range(len(s) - 2):
        if s[i] == "x":
            if s[i + 1] == "x":
                if s[i + 2] == "x":
                    return True
                else:
                    return False
            else:
                return False
    return False


print(triple_x(""))
print(triple_x(" "))
print(triple_x("softXXX kitty, warm kitty, xxxxx"))
print(triple_x("softx kitty, warm kitty, xxxxx"))
