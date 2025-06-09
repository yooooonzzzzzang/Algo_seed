
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String[] arr = new String[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.next();
    }

    Arrays.sort(arr, new Comparator<String>() {
      @Override
      public int compare(String o1, String o2) {
        if (o1.length() == o2.length()) {
          int o1Cnt = 0;
          int o2Cnt = 0;
          for (int i = 0; i < o1.length(); i++) {
            if (o1.charAt(i) < 65) {
              o1Cnt += Integer.parseInt(o1.charAt(i) + "");
            }
          }
          for (int i = 0; i < o2.length(); i++) {
            if (o2.charAt(i) < 65) {
              o2Cnt += Integer.parseInt(o2.charAt(i) + "");
            }
          }
          if (o1Cnt == o2Cnt) {
            return o1.compareTo(o2);
          }
          return o1Cnt - o2Cnt;
        }
        return o1.length() - o2.length();
      }
    });
    for (String s : arr) {
      System.out.println(s);
    }
  }
}
