import java.util.regex.*;

public class StripComments {

  public static String stripComments(String text, String[] commentSymbols) {
    StringBuilder patternBuilder = new StringBuilder("[");
    for (String symbol : commentSymbols) {
      // Escape regex special characters
      patternBuilder.append(Pattern.quote(symbol));
    }
    patternBuilder.append("].*$");

    // Compile pattern with MULTILINE mode so ^ and $ work per line
    Pattern pattern = Pattern.compile(patternBuilder.toString(), Pattern.MULTILINE);

    // Replace all comment parts with empty string
    Matcher matcher = pattern.matcher(text);
    String cleaned = matcher.replaceAll("");

    // Trim trailing spaces at end of each line
    cleaned = cleaned.replaceAll("[ \\t]+(?=\\n|$)", "");

    Sy

    return cleaned;
  }

}

//import java.util.Arrays;
//import java.util.stream.Collectors;
//
//public class StripComments {
//
//  public static String stripComments(String text, String[] commentSymbols) {
//    String pattern = String.format(
//        "[ ]*([%s].*)?$",
//        Arrays.stream( commentSymbols ).collect( Collectors.joining() )
//    );
//    return Arrays.stream( text.split( "\n" ) )
//        .map( x -> x.replaceAll( pattern, "" ) )
//        .collect( Collectors.joining( "\n" ) );
//  }
//
//}