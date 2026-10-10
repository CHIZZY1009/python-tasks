import random

def random_numbers():
    random_number = []
    for index in range(0,10):
        numbers = random.randint(0,50)
        random_number.append(numbers)
    return random_number

print(random_numbers())


def list_length(number):
     count = 0
     for index in number:
         count += 1
     return count


print(list_length([10,20,30]))


def even_positions(list):
    even_index_sum = 0


    for index in range(len(list)):
        if index % 2 == 0:
           even_index_sum += list[index]
    return even_index_sum



print(even_positions([12,20,30,40,50]))
    
    

def odd_positions(list):
    odd_index_sum = 0


    for index in range(len(list)):
        if index % 2 != 0:
           odd_index_sum += list[index]
    return odd_index_sum



print(odd_positions([12,20,30,40,50]))



def product_of_third_position(number):
    product = 1
    for index in range(len(number)):
        if index % 3 == 0:
             product *= number[index]
    return product 

print(product_of_third_position([1,2,3,4,5,6,7,8,9]))


def largest(number):
    largest = number[0]
    for index in range(len(number)):
        if number[index] > largest:
            largest = number[index] 
    return largest
            

print(largest([1,2,3,4,5]))



def smallest(number):
    smallest = largest([5,2,3,4,5])
    for index in range(len(number)):
        if number[index] < smallest:
            smallest = number[index] 
    return smallest
            

print(smallest([5,1,3,4,5]))
