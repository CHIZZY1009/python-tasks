
number = input("Enter a Number: ")
smallest = 9
for digit in number:
    if int(digit) < smallest:
        smallest = int(digit)
print("The Smallest number is:  ",digit)
