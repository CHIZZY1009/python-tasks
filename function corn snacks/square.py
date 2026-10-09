def square_list(numbers):
    result = []

    for number in numbers:
        result.append(number ** 2)

    return result


print(square_list([2, 3, 4, 5, 7]))