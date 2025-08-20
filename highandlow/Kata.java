public class Kata {
  public static String highAndLow(String numbers) {
    int max = Integer.MIN_VALUE;
    int min = Integer.MAX_VALUE;
    String[] numbersArray = numbers.split(" ");
    for (int i = 0; i < numbersArray.length; i++){
      int num = Integer.parseInt(numbersArray[i]);
      if (num > max){
        max  = num;
      }
      if (num < min){
        min  = num;
      }
      }
    String output = String.format("%d %d", max, min);
    return output;
  }

}
// Community Solution
// https://www.codewars.com/kata/554b4ac871d6813a03000035/train/java

// import static java.util.Arrays.stream;

// class Kata {
//   static String highAndLow(String numbers) {
//     var stats = stream(numbers.split(" ")).mapToInt(Integer::parseInt).summaryStatistics();
//     return stats.getMax() + " " + stats.getMin();
//   }
// }
