
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String A = scanner.next();
    String B = scanner.next();
    int ans = 50;
    for (int i = 0; i < B.length()-A.length()+1; i++) {
      int tmp =0;
      for (int j = 0; j < A.length(); j++) {
        if (A.charAt(j) == B.charAt(i+j)) {
          tmp += 1;
        }
      }
      ans = Math.min(ans, A.length() - tmp);
    }
    System.out.println(ans);
  }
}
