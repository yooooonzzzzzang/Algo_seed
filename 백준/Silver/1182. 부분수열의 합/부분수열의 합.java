
import java.util.Scanner;

public class Main {
  static int[] arr;
  static int n;
  static int s;
  static int ans;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    s = sc.nextInt();
    arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    recur(0, 0);
    if(s==0) ans --;
    System.out.println(ans);

  }

  static void recur(int dept, int total){
    if (dept == n){
      if (total == s)ans ++;
      return;
    }
      recur(dept + 1, total + arr[dept]);
      recur(dept + 1, total);
  }
}
