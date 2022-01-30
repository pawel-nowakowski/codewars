def delete_nth(order,max_e):
    noDupes = list(set(order))
    for i in noDupes:
        n = 0
        x = 0
        while n < len(order):
            if i == order[n]:
                x += 1
                if x > max_e:
                    del order[n]
                    n -= 1
            n += 1
    print(order)

delete_nth([23, 4, 28, 28, 48, 31, 31, 48, 28, 31, 48, 31, 31, 31, 4, 48, 28, 28, 28, 28, 31, 48, 48, 28, 28], 4)
delete_nth([1,2,3,1,2,1,2,3], 2)
delete_nth([20,37,20,21], 1)
delete_nth([1,1,3,3,7,2,2,2,2], 3)