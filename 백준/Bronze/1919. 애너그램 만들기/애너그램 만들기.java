import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str1  = br.readLine().toLowerCase();
    String str2  = br.readLine().toLowerCase();
    int ans = 0;
    int[] check = new int[26];
    int[] check2 = new int[26];
    for (int i = 0; i < str1.length(); i++) {
      check[str1.charAt(i) - 'a'] += 1;
    }
    for (int i = 0; i < str2.length(); i++) {
      check2[str2.charAt(i) - 'a'] += 1;
    }
    for (int i = 0; i < check.length; i++) {
      ans += Math.abs(check[i] - check2[i]);
    }
    System.out.println(ans);
  }
}
