// Basic Implementation
public class Solution {

  public int solution(int number) {
    int sum = 0;
    for (int i = 3; i < number; i++){
      if((i % 3 == 0) | (i % 5 == 0)){
        sum += i;
      }
    }
    return sum;
  }
}

// Consider Implementing via IntStream
// Community Solution
// public class Solution {

//   public int solution(int number) {
//   	int sum=0;
    
//     for (int i=0; i < number; i++){
//     	if (i%3==0 || i%5==0){sum+=i;}
//     }
//     return sum;
//   }
// }
