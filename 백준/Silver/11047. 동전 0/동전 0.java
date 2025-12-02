
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int[] arr = new int[n];
    for(int i=0; i<n; i++){
      arr[i] = sc.nextInt();
    }
    int ans = 0;
    // 백트래킹이런거 없이 무조건 큰 동전을 먼저 사용하는게 정답
    // 그리디
    for (int i = n-1; i > -1; i--) {
      if (k == 0) break;
      if (arr[i] <= k){
        ans += k / arr[i];
        k %= arr[i];
      }
    }
    System.out.println(ans);
  }
}
