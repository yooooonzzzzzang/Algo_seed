import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int[] dp = new int[k + 1];
    Arrays.fill(dp, 100001);
    dp[0] = 0;

    int[] coin = new int[n];
    for (int i = 0; i < n; i++) {
      coin[i] = sc.nextInt();
      if(coin[i] <= k) dp[coin[i]] = 1;
    }
    for(int i=1; i<=k; i++){
      for(int j=0; j<n; j++){
        if(i-coin[j]>=0) {
          dp[i] = Math.min(dp[i - coin[j]] + 1, dp[i]);
        }
      }
    }

    System.out.println(dp[k] == 100001 ? -1: dp[k]);

  }
}
