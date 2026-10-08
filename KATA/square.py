def isSquare(number):
    if number < 0:
        return 'False'
    for i in range (1,number+1):
        if i * i == number:

            return 'True'

    return 'False'



print(isSquare(25))

