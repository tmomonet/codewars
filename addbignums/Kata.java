
public class Kata {
  public static String add(String a, String b) {
    
    a = a.replaceFirst("^0+(?!$)", "");
    b = b.replaceFirst("^0+(?!$)", "");
    
    int i = a.length() - 1;
    int j = b.length() - 1;
    int carry = 0;
    
    StringBuilder output = new StringBuilder();
    
    while (i >= 0 || j >= 0 || carry > 0){
      int digitA = (i >= 0) ? a.charAt(i) - '0' : 0;
      int digitB = (j >= 0) ? b.charAt(j) - '0' : 0;

      int sum = digitA + digitB + carry;
      carry = sum / 10;            // if sum >= 10, carry 1 to the next column
      int currentDigit = sum % 10; // the digit to write down

      output.append(currentDigit);

      i--;
      j--;
    }
    return output.reverse().toString();
  }
}
