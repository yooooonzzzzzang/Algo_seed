
import java.util.Scanner;

public class Main {
  static int n;
  static int[][] arr;
  static boolean[] visited;
  static int ans = Integer.MAX_VALUE;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    arr = new int[n][n];
    visited = new boolean[n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        arr[i][j] = sc.nextInt();
      }
    }

    recur(0,0,0,0);
    System.out.println(ans);

  }

  static void recur(int start, int node, int sum, int cnt){
    if (start == node && cnt == n){
      // 계산
      ans = Math.min(ans, sum);
      return;
    }
    for (int i = 0; i < n; i++) {
      if (!visited[i] && arr[node][i] != 0) {
        visited[i] = true;
        recur(start, i, sum + arr[node][i], cnt + 1);
        visited[i] = false;
      }
    }
  }
}
