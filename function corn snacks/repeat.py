def repeat_string(string, number):
    if isinstance(number, float):
        return string

    return string * number


print(repeat_string("hello", 3))
print(repeat_string("hi", 4.5))