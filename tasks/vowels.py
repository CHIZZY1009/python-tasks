text = input(str("Enter a string: "))
count = 0
for letter in text:
    if letter in "aeiouAEIOU":
        count+=1
print("The Number of vowels are: ",count, )
