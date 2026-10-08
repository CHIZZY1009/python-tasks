def isPalindrome(number):
        for i in range(1,number):
            for index_two in range (number,1,-1):
                if i == index_two:
                    return 'True'
        return 'False'
    



print(isPalindrome(54145))
