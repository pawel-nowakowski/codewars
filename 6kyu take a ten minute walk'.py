def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        vertical = 0
        horizontal = 0
        for i in walk:
            if i == 'n':
                vertical += 1
            elif i == 's':
                vertical -= 1
            elif i == 'w':
                horizontal += 1
            elif i == 'e':
                horizontal -= 1
        if vertical == 0 and horizontal == 0:
            return True
        else:
            return False
is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])