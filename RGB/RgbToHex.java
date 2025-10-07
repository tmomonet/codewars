// https://www.codewars.com/kata/513e08acc600c94f01000001/solutions/java

import java.lang.Integer;

public class RgbToHex {

    public static String rgb(int r, int g, int b) {
      String output = toHex(r) + toHex(g) + toHex(b);
      return output;      
    }
    
    public static String toHex(int color) {
      if (color < 0){
        return "00";
      }
      if (color > 255){
        return "FF";
      }
      String hex = Integer.toHexString(color).toUpperCase();
      if (hex.length() == 1) hex = "0" + hex;
      return hex;
    }
  
}

// Community Solution
//   public class RgbToHex {

//     public static String rgb(int r, int g, int b) {
//         return String.format("%02X%02X%02X", verify(r), verify(g), verify(b));
//     }

//     private static int verify(int i) {
//         return i > 0 ? Math.min(255, i) : 0;
//     }
// }
