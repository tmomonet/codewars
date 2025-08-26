//https://www.codewars.com/kata/517abf86da9663f1d2000003/train/java

import java.lang.StringBuilder;
import java.util.Arrays;
class Solution{
  static String toCamelCase(String s){
    String regex = "[_-]";
    String [] splitter = s.split(regex);
    StringBuilder camelCase = new StringBuilder();
    System.out.println(Arrays.toString(splitter));
    for (int i  = 0; i < splitter.length; i++){
      if (i == 0){
        camelCase.append(splitter[i]);
      } else {
        camelCase.append(splitter[i].substring(0, 1).toUpperCase());
        camelCase.append(splitter[i].substring(1).toLowerCase());
      }
    }
    return camelCase.toString();
  }
}

//Community Solution
//import java.util.Arrays;
//
//class Solution{
//
//  static String toCamelCase(String str){
//    String[] words = str.split("[-_]");
//    return Arrays.stream(words, 1, words.length)
//        .map(s -> s.substring(0, 1).toUpperCase() + s.substring(1))
//        .reduce(words[0], String::concat);
//  }
//}
