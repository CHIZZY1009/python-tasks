number = input("Enter a Number: ")
largest = 0
for digit in number:
    if int(digit) > largest:
        largest = int(digit)
print("The largest number is:  ",digit)
