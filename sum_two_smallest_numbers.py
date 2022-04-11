def sum_two_smallest_numbers(numbers):
    num1 = min(numbers)
    numbers.remove(num1)
    num2 = min(numbers)
    sum_ = num1 + num2
    print(sum_)
    return sum_


sum_two_smallest_numbers([5, 8, 12, 18, 22])
