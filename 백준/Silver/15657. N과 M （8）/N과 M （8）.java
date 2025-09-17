
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static int n, m;
  static int arr[];
  static int ans[];
  static boolean visited[];
  static StringBuilder sb = new StringBuilder();

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    m = sc.nextInt();
    arr = new int[n];
    ans = new int[m];

    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    Arrays.sort(arr);

    recur(0, 0);
    System.out.println(sb);
  }
  static void recur(int dept, int start) {
    if (dept == m){
      for (int i = 0; i < m; i++) {
        sb.append(ans[i] + " ");
      }
      sb.append("\n");
      return;
    }
    for (int i = start; i < n; i++){
      ans[dept] = arr[i];
      recur(dept + 1, i);
    }
  }
}
