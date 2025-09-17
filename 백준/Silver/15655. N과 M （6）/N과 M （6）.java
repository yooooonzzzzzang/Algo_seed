
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static int n, m;
  static int arr[];
  static int ans[];
  static boolean visited[];
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    m = sc.nextInt();
    arr = new int[n];
    ans = new int[m];
    visited = new boolean[n];

    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    Arrays.sort(arr);
    recur(0, 0);
  }

  static void recur(int dept, int start) {
    if (dept == m) {
      StringBuilder sb = new StringBuilder();
      for(int i=0; i<m; i++) {
        sb.append(ans[i] + " ");
      }
      System.out.println(sb);
      return;
    }
    for (int i = start; i < arr.length; i++) {
      if (!visited[i]) {
        visited[i] = true;
        ans[dept] = arr[i];
        recur(dept + 1, i+1);
        visited[i] = false;
      }
    }
  }
}
