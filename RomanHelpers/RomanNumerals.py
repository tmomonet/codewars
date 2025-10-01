# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

class RomanNumerals:
     
    romanArabicDict = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}
    
    @staticmethod
    
    def to_roman(val : int) -> str:
        output = ""
        for number, letters in RomanNumerals.romanArabicDict.items():
            while val >= number:
                val -= number
                output += letters
        return output

    @staticmethod
    def from_roman(roman_num : str) -> int:
        stack = []
        str = list(roman_num)
        #Invert Dictionary
        invDict = {v: k for k, v in RomanNumerals.romanArabicDict.items()}
        
        for letter in str:
            value = invDict[letter]
            
            if (len(stack) > 0 and stack[-1] < value):
                value = value - stack.pop()
        
            stack.append(value)
        return sum(stack)
        
