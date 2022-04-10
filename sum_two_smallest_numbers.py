def sum_two_smallest_numbers(numbers):
    num1, num2 = 0, 0
    num1 = min(numbers, key=lambda i: int(i))
    numbers.remove(num1)
    num2 = min(numbers, key=lambda i: int(i))
    sum_ = num1 + num2
    print(sum_)
    return sum_


sum_two_smallest_numbers([5, 8, 12, 18, 22])
