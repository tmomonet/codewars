import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static int[] twoSum(int[] numbers, int target) {
      // Adds seen value to reduce computational complexity on successive loops
      Map<Integer, Integer> seen = new HashMap<>();
      for (int i = 0; i < numbers.length; i++){
        // Loop through and check if complement to value has been seen already
        int complement = target - numbers[i];
        // If so include in sum pairs
        if (seen.containsKey(complement)){
          return new int[]{seen.get(complement), i};
        }
        seen.put(numbers[i], i);
        }
      return null; // no pair
    }
}


// Community Solution
// public class Solution
// {
//     public static int[] twoSum(int[] numbers, int target)
//     {
//        for(int i = 0; i < numbers.length; i++) {
//            for(int j = i + 1; j < numbers.length; j++) {
//                if(numbers[i] + numbers[j] == target){
//                    return new int[]{i, j};
//                }
//            }
//        }
//       return null; 
//     }
// }
