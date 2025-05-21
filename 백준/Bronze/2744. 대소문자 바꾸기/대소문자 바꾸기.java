
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    List<String> ans = new ArrayList<>();
    String s = scanner.nextLine();
    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (c >= 65 && c <= 90) {
        ans.add(String.valueOf(c).toLowerCase());
      } else ans.add(String.valueOf(c).toUpperCase());
    }

    System.out.println(String.join("", ans));

  }
}