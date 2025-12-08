
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  // 여러 동전의 개수가 한정되었을때 T 가 될 수 있는 조합
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int t = sc.nextInt();
    int k = sc.nextInt();
    int[][] dp = new int[k+1][t+1];
    dp[0][0] = 1;

    for (int i = 1; i <= k; i++) {
      int coinPrice = sc.nextInt();
      int coinCount = sc.nextInt();
      for (int value = 0; value <= t; value++) {
        for (int cnt = 0; cnt <= coinCount; cnt++) {
          int nextValue = value + coinPrice * cnt;
          if(nextValue > t) break;
          dp[i][nextValue] += dp[i-1][value];
        }
      }
    }
    System.out.println(dp[k][t]);
  }
}
