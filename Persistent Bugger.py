"""
    Write a function, persistence, that takes in a positive parameter num and returns
its multiplicative persistence,
which is the number of times you must multiply the digits in
num until you reach a single digit.

"""


def persistence(n):
    n = str(n)
    answer = 1
    i, number = 0, 0
    while True:
        while i < len(n):
            answer *= int(n[i])
            i = i + 1
        if int(n) < 10:
            break
        number += 1
        i = 0
        n = answer
        answer = 1
        n = str(n)
    return number

persistence(39)
