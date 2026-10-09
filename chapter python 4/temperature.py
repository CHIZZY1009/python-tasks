def fahrenheit(number):
 celcius = number
 fahrenheit =  (9 / 5) * celcius + 32
 return fahrenheit





for i in range(0, 101):
    result = fahrenheit(i)
    print(f"{result:.1f}")
