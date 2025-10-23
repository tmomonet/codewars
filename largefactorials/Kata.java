import java.math.BigInteger;

public class Kata
{

  public static String Factorial(int n) {
    if (n == 0) {
      return "1";
    }
    if (n < 0){
      return null;
    }
    BigInteger product = BigInteger.ONE;
    return String.valueOf(recursiveHelper(n));
  }

  private static BigInteger recursiveHelper(int n) {
    return (n > 1) ? recursiveHelper(n - 1).multiply(BigInteger.valueOf(n)) : BigInteger.ONE;
  }
}
