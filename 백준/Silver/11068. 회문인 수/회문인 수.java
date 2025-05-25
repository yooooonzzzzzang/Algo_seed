
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int T = scanner.nextInt();
    for (int i = 0; i < T; i++) {
      int N = scanner.nextInt();
        if (numberSystem(N)) {
          System.out.println(1);
        } else{
          System.out.println(0);
        }
      }

    }

  private static boolean numberSystem(int N) {

    for (int i = 2; i <= 64; i++) {
      int n = N;
      // 2^20 이 백만정도
      int[] ans = new int[20];
      int index = 0;
      while (n > 0) {
        int divid = n % i;
        ans[index++] = divid;
        n /= i;
      }
      if (isPalindrome(ans, index)){
        return true;
    }
  }
    return false;
  }

  private static boolean isPalindrome(int[] ans, int len) {
    for (int i = 0; i < len / 2; i++) {
      if (ans[i] != ans[len - 1 - i]) {
        return false;
      }
    }
    return true;
  }

}
