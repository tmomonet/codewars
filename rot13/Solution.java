class Solution {
  
   public static String rot13(String message) {
     // alphabet strings
     String abc = "abcdefghijklmnopqrstuvwxyz";
     String ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

     // Message as a chArry
     char[] charMessage = message.toCharArray();

     // Instantiate StringBuilder
     StringBuilder sb =  new StringBuilder();

     // Loop through
     for (int i = 0; i < charMessage.length; i++){
       // Codepoint cast to int
       int cp = (int) charMessage[i];

       // check for uppercase and append accordingly
       if (cp <= 90 && cp >= 65){
         cp  = (cp - 52) % 26;
         sb.append(ABC.charAt(cp));
       }
         // check for lowercase and append accordingly
       else if (cp <= 122 && cp >= 97){
         cp  = (cp - 84) % 26;
         sb.append(abc.charAt(cp));
       }
         //otherwise
       else {
         sb.append(charMessage[i]);
       }
     }
      return sb.toString();
   }
  
}
