https://www.codewars.com/kata/526d84b98f428f14a60008da/train/java

import java.util.List;
import java.util.ArrayList;

public class Hamming {

	public static long hamming(int n) {
  	List<Long> nums = new ArrayList<>();
    nums.add(1L);
    int i2 = 0;
    int i3 = 0;
    int i5 = 0;
    
    while (nums.size() < n){
      long next2 = nums.get(i2) * 2;
      long next3 = nums.get(i3) * 3;
      long next5 = nums.get(i5) * 5;
      
      long next_num = Math.min(Math.min(next2, next3), next5);
      nums.add(next_num);
      
      if (next_num == next2){
        i2++;
      }
      if (next_num == next3){
        i3++;
      }
      if (next_num == next5){
        i5++;
      }
    }
    return nums.get(nums.size() - 1);
  }
}


Community Solution
public class Hamming {
	
  public static long hamming(int n) {
    long[] h = new long[n];
    h[0] = 1;
    long x2 = 2, x3 = 3, x5 = 5;
    int i = 0, j = 0, k = 0;
 
    for (int index = 1; index < n; index++) {
      h[index] = Math.min(x2, Math.min(x3, x5));
      if (h[index] == x2) x2 = 2 * h[++i];
      if (h[index] == x3) x3 = 3 * h[++j];
      if (h[index] == x5) x5 = 5 * h[++k];
    }
    
    return h[n - 1];
  }
