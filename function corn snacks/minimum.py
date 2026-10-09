def minimum(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


print(minimum([8, 4, 9, 2, 5, 7, 3]))