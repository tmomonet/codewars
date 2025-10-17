# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python

def is_interesting(number, awesome_phrases):
    
    if (numCheck((number), awesome_phrases)) == 2:
        return 2
    elif (numCheck((number + 1), awesome_phrases) == 2) or (numCheck((number + 2), awesome_phrases) == 2):
        return 1
    else:
        return 0
    

def numCheck(num, phrase_list):
    
    #convert to string for iteration
        numStr = str(num)
        
        trailing0= True
        monotone = True
        awesome = True
        palindromic = True
        increment = True
        decrement = True
        
    #check for 3 digits
        if (num < 100):
            return 0
    
    #Check length
        exponent = 10 ** (len(numStr) - 1)
    #Handle numbers that end in consecutive 0s            
        if (num % exponent) != 0:
            trailing0 = False
        
        #Palindromic
        if numStr != numStr[::-1]:
            palindromic = False
        #Check if awesome
        for nums in phrase_list:
            if num == nums:
                return 2
    
        #loop compare, if false, set accordingly
        for i in range(1, len(numStr)):
            val1 = int (numStr[i - 1]) 
            val2 = int (numStr[i])
            if val1 != val2:
                monotone = False
            if (val1 + 1) % 10 != ((val2 % 10)):
                increment = False
            if (val1 - 1)!= ((val2 % 10)):
                decrement = False
        #if any true, return 2
        if trailing0 or monotone or palindromic or increment or decrement:
            print(trailing0, monotone, palindromic, increment, decrement)
            return 2
        else:
            return 0


# Community Solution

# def is_incrementing(number): return str(number) in '1234567890'
# def is_decrementing(number): return str(number) in '9876543210'
# def is_palindrome(number):   return str(number) == str(number)[::-1]
# def is_round(number):        return set(str(number)[1:]) == set('0')

# def is_interesting(number, awesome_phrases):
#     tests = (is_round, is_incrementing, is_decrementing,
#              is_palindrome, awesome_phrases.__contains__)
       
#     for num, color in zip(range(number, number+3), (2, 1, 1)):
#         if num >= 100 and any(test(num) for test in tests):
#             return color
#     return 0
