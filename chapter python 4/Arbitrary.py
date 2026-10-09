def product_numbers(*numbers):
    product = 1
    for i in numbers: 

        product =  product * i
    return product
    


    
print(product_numbers(2, 4, 6, 8 ))
