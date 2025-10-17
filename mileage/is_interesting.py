# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python

def is_interesting(number, awesome_phrases):
    
    if (numCheck((number + 1), awesome_phrases) == 2) or (numCheck((number + 2), awesome_phrases) == 2):
        return 1
    else:
        return(numCheck((number), awesome_phrases))
    

def numCheck(num, phrase_list):
    
        numStr = str(num)
    
        if (num < 100):
            return False
    
        if numStr == numStr[::-1]:
            return 2
    
        for nums in phrase_list:
            if num == nums:
                return 2
            
        return False
