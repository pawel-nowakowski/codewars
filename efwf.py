a = [[1,2,3],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]]
for i in range(len(a)):
    if a[i][:2] == [1,2]:
        del a[i]
        break

print(a)