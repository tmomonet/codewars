class YesOrNo
{
  public static String boolToWord(boolean b)
  {
    // Check for True
    if (b) {
    return "Yes"
    }
    // Check for No
    if (!b) {
    return "No"
    }
    // If neither is met, return null
    return null;
  }
  
}
