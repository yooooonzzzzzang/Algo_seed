import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {
  static String ans ;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    while (t-- > 0) {
      int n = sc.nextInt();
      int m = sc.nextInt();
      int[]v = new int[10000];
      String[]road = new String[10000];
      Deque<Integer> queue = new ArrayDeque<>();
      queue.add(n);
      v[n] = 1;
      road[n] = "";
      while (!queue.isEmpty()) {
        int num = queue.poll();
        if (num == m) {
          System.out.println(road[num]);
          break;
        }
        int d = funD(num);
        int s = funS(num);
        int l = funL(num);
        int r = funR(num);
        if (v[d] == 0){
          queue.add(d);
          road[d] = road[num] + "D";
          v[d] = 1;
        }
        if (v[s] == 0){
          queue.add(s);
          road[s] = road[num] + "S";
          v[s] = 1;
        }
        if (v[l] == 0){
          queue.add(l);
          road[l] = road[num] + "L";
          v[l] = 1;
        }
        if (v[r] == 0){
          queue.add(r);
          road[r] = road[num] + "R";
          v[r] = 1;
        }
      }
    }
  }
  static int funD(int n) {
    return 2*n%10000;
  }

  static int funS(int n) {
    return n -1 < 0 ? 9999 : n-1;
  }

  // 1 2 3 4
  // 2 3 4 1
  static int funL(int n) {
    return (n % 1000 ) * 10 + n / 1000;
  }
  // 1 2 3 4
  // 4 1 2 3
  static int funR(int n) {
    return n % 10 * 1000 + n /10;
  }
}
