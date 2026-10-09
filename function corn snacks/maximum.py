def maximum(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


print(maximum([8, 4, 9, 2, 5, 7, 3]))