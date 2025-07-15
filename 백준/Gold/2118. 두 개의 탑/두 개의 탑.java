
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static int n;
  static int [] arr;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }

    int prefix [] = new int[2*n+1];
    for (int i = 0; i < 2*n; i++) {
      prefix[i+1] = prefix[i] + arr[i % n];
    }

    int ans = 0;
    int total = Arrays.stream(arr).sum();
    int right = 1;
    
    for (int i = 1; i < 2*n; i++) {
      while (right < 2 * n + 1 && prefix[right] - prefix[i] <= total - prefix[right] + prefix[i]) {
        ans = Math.max(ans, prefix[right] - prefix[i]);
        right += 1;
      }
    }
    System.out.println(ans);






  }
}
