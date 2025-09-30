// CodeWars Java implementation of RomanNumerals
// https://www.codewars.com/kata/51b66044bce5799a7f000003/train/java

import java.util.Stack;

public class RomanNumerals {
 
  public static String toRoman(int n) {
    String[] letters = {"M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"}
    ;
    
    int[] lookupValues = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    String output = "";
    for(int i = 0; i < lookupValues.length; i++){
      while (n >= lookupValues[i]){
        n -= lookupValues[i];
        output += letters[i];
      }
    }
    return output;
  }
  
  public static int fromRoman(String romanNumeral) {
    Stack<Integer> stack = new Stack<>();
    
    for (char c : romanNumeral.toCharArray()) {
      int value = valueOf(c);
      
      if (!stack.isEmpty() && stack.peek() < value) {
        value = value - stack.pop();
      }
      stack.push(value);
    }
    int total = 0;
    
    while (!stack.isEmpty()){
      total += stack.pop();
    }
    return total;
  }
  
  private static int valueOf(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: throw new IllegalArgumentException("Invalid Roman numeral: " + c);
        }
    }
}


// Community Solution
// public class RomanNumerals {
//     private static final String[] ROMAN_NUMBERS = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
//     private static final int[] ARABIC_NUMBERS = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

//     public static String toRoman(int n) {
//         int remainingValue = n;
//         StringBuilder result = new StringBuilder();

//         for (int i = 0; i < ARABIC_NUMBERS.length; i++) {
//             while (remainingValue >= ARABIC_NUMBERS[i]) {
//                 remainingValue -= ARABIC_NUMBERS[i];
//                 result.append(ROMAN_NUMBERS[i]);
//             }
//         }

//         return result.toString();
//     }

//     public static int fromRoman(String romanNumeral) {
//         String remainingValue = romanNumeral;
//         int result = 0;

//         for(int i = 0; i<ROMAN_NUMBERS.length; i++) {
//             while(remainingValue.startsWith(ROMAN_NUMBERS[i])) {
//                 remainingValue = remainingValue.substring(ROMAN_NUMBERS[i].length(), remainingValue.length());
//                 result += ARABIC_NUMBERS[i];
//             }
//         }
//         return result;
//     }
// }
