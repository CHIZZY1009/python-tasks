def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total

print(sum_of_squares([2, 3, 4, 5, 7]))  # 103