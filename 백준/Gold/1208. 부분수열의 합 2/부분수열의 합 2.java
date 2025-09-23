
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
// n이 40 2^40 1초 불가 (1초 1억) 2^20 = 100만
// 절반으로 나눠서 (2^20) S-s1 = s2 이면 됨 -> 맵으로 s1 = S-s2 찾는다.
public class Main {
  static int n, s;
  static long ans;
  static int[]arr;
  static int status = -1;
  static final int LEFT = 0;
  static final int RIGHT = 1;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    s = sc.nextInt();
    arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    status = LEFT;
    recur(0, n/2, 0);

    status = RIGHT;
    recur(n/2, n, 0);

    if (s ==0) ans --;
    System.out.println(ans);

  }

  static Map<Integer, Integer> map = new HashMap<>();
  public static void recur(int index,int end, int sum) {
    //base
    if (index == end) {
      // 결과값 저장
      if (status == LEFT){
        int prev = map.getOrDefault(sum, 0);
        map.put(sum, prev+1);
      } else {       // s - sum
        ans += map.getOrDefault(s-sum, 0);
      }
      return ;
    }
    //recur
    recur(index+1, end, sum);
    recur(index+1, end, sum+arr[index]);


  }
}
