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
        return 0
