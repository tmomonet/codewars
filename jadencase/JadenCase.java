import java.lang.String;

public class JadenCase {
  StringBuilder output = new StringBuilder();
  
	public String toJadenCase(String phrase) {
		if (phrase == null || phrase.isEmpty()){
      return null;
    }
    String[] jaden = phrase.split(" ");
    System.out.println(jaden.length);
		
    for (String word: jaden){
      String capitalized =
          Character.toUpperCase(word.charAt(0)) +
          word.substring(1);

      output.append(capitalized).append(" ");
    }
		return output.toString().trim();
	}

}

// Community Solution

//   import java.lang.Character;

// public class JadenCase {

// 	public String toJadenCase(String phrase) {
//     if(phrase == null || phrase.equals("")) return null;
    
//     char[] array = phrase.toCharArray();
    
//     for(int x = 0; x < array.length; x++) {
//       if(x == 0 || array[x-1] == ' ') {
//         array[x] = Character.toUpperCase(array[x]);
//       }
//     }
		
// 		return new String(array);
// 	}

}
