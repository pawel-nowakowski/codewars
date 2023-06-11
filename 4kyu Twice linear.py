u = [1]
for indexU in range(300000):
    y = 2 * u[indexU] + 1
    z = y + u[indexU]
    u.append(y)
    u.append(z)
u = sorted(list(set(u)))


def dbl_linear(n):
    return u[n]


print(u)
print(len(u))
print(dbl_linear(60000))
