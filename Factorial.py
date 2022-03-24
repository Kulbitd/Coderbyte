def first_factorial(num):
    res = 1
    size = 1
    while size < num + 1:
        res *= size
        size += 1
    return res


print(first_factorial(int(input())))
