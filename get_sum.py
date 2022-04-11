"""
Given two integers a and b, which can be positive or negative,
 find the sum of all the integers between and including them
 and return it. If the two numbers are equal return a or b.
"""


def get_sum(a, b):
    if a == b:
        return a
    answer = []
    one = min(a, b)
    while max(a, b) >= one:
        answer.append(one)
        one += 1
    answer = sum(answer)
    print(answer)


get_sum(0, 8)