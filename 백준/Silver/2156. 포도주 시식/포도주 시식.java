import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr = new int[n+1];
    for (int i = 1; i <= n; i++) {
      arr[i] = sc.nextInt();
    }
    int[] dp = new int[n+2];

    dp[1] = arr[1];
    if(n>1)dp[2] = dp[1] + arr[2];
    if (n >2) {
        for (int i = 3; i <= n; i++) {
          // 1.현재 포도주를 마시지않는경우
          // 2.현재 포도주 마시고 그 전포도주는 마시지 않는 경우
          // 3.현재와 그 직전포도주를 마시는 경우
          dp[i] = Math.max(dp[i-1], Math.max( dp[i-2]+arr[i],  dp[i-3] + arr[i-1] + arr[i]));
        }
    }
    System.out.println(dp[n]);
  }
}
