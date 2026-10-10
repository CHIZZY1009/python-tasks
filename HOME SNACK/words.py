def length_of_string():
    total = []
    words = ['zida', 'is', 'a', 'gogo','girl']
    length_of_words = len(words)
    for word in words:
        if len(word) > 2 and word[:2] == word[-2:]:
            total.append(word)
    

    return length_of_words,total
    
    
print(length_of_string())


def list_of_integers():
    total = []
    for index in range(16):
        total.append(index)

    return total


print(list_of_integers())




def add_three_items(number):
     sum_of_third_numbers = 1
     for index in range(len(number)):
        if index % 3 == 0:
            sum_of_third_numbers += number[index]
     return sum_of_third_numbers

print(add_three_items([1,2,3,4,5,6,7,8,9,1,2,3,4,5]))



