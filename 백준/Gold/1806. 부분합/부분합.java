
import java.util.Scanner;

public class Main {
  static int n;
  static int s;
  static int[]arr;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    s = sc.nextInt();
    arr = new int[n];

    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    // 답이 될수없는 값을 둠
    int ans = n+1;
    int r = 0;
    int sum = arr[0];

    for (int i = 0; i < n; i++) {
      while (sum < s && r < n-1){
        sum += arr[++r];
      }
      if (sum >= s){
        ans = Math.min(ans, r-i+1);
      }
      sum -= arr[i];
    }
    if (ans > n) {ans = 0;}
    System.out.println(ans);

  }
}
