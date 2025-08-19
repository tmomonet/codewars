// https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/java

public class BraceChecker {

  public boolean isValid(String braces) {
    char[] chars = braces.toCharArray();
    HashMap<Character, Character> map = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
    };

    if (braces.length() % 2 != 0) {
      return false;
    }
    Stack stack = Stack();
    for (int i = 0; i < chars.length; i++) {
        if (chars[i] == '(' || chars[i] == '[' || chars[i] == '{'){
          stack.push(chars[i])
        }
        if (chars[i] == ')' || chars[i] == ']' || chars[i] == '}'){
          if (stack.top == map.get(chars[i])){
            stack.pop()
          }
        }
    }
    if (!stack.empty){
      return false;
    }
  }

}
