
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    String s = scanner.next();
    int n = scanner.nextInt();
    int ans = 0;
    for (int i = 0; i < s.length(); i++) {
      int tmp ;
      char ch = s.charAt(i);
      if (ch >'9') tmp = ch -'A' + 10;
      else tmp = ch - '0';
      ans = ans * n + tmp;
    }
    System.out.println(ans);
  }
}
