
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();

    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }

    Arrays.sort(arr);
    int s =0, e=0;
    int ans = 2000000000;
    while (true){
      if (s > n-1 || e > n-1){
        break;
      }
      int abs = Math.abs(arr[s] - arr[e]);
      if (abs < m){
        e ++;
      } else{
        ans = Math.min(ans,abs);
        s ++;
      }
    }
    System.out.println(ans);

  }
}
