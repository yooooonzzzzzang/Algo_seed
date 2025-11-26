
import java.util.Scanner;

public class Main {
  static int[] arr;
  static int[] v;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    while (T-- > 0) {
      int n = sc.nextInt();
      arr = new int[n+1];
      for (int i = 1; i <= n; i++) {
        arr[i] = sc.nextInt();
      }

      v = new int[n+1];
      int ans = 0;
      for (int i = 1; i <= n; i++) {
        if (v[i] == 0){
          dfs(i);
          ans++;
        }
      }
      System.out.println(ans);
    }
  }
  static void dfs(int x){
    if (v[x] == 1) return;
    v[x] = 1;
    dfs(arr[x]);

  }
}

