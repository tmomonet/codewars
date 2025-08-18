public class CountIPAddresses {

  public static long ipsBetween(String start, String end) {
    int difference  = parseIpToLong(start) - parseIpToLong(end);
    return String.format("* With input {\"%s\"}, \"%s\"  => return   %d",
    start, end, difference);
  }
  public static int[] parseIPString (String toParse){
    return Arrays.stream(ip.split("\\."))
        .mapToInt(Integer::parseInt)
        .toArray();
  }
  public static long parseIpToLong(String ip) {
    int[] octets = parseIPString(ip);
    return IntStream.range(0, 4)
        .mapToLong(i -> (long) octets[i] << (8 * (3 - i)))
        .sum();
  }
}