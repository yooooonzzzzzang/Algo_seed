
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
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
    recur(0);
    System.out.println(sb);


  }
  static StringBuilder sb = new StringBuilder();
  private static void recur(int dept) {
    if(dept == m){
      for (int i = 0; i < m; i++) {
        sb.append(ans[i] +" ");
      }
      sb.append("\n");
      return;
    }
    for (int i = 0; i < arr.length; i++) {
      ans[dept] = arr[i];
      recur(dept + 1);
    }
  }
}
