
import java.util.Scanner;

public class Main {
  static int alpCnt =0;
  static int[] alp = new int[26];

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    char[] arr = sc.next().toCharArray();
    int ans = 0;
    int nextIdx = 0;
    for (int i = 0; i < arr.length; i++) {
      while (nextIdx < arr.length ){
        alpIncrease(arr[nextIdx++] - 'a');
        if (alpCnt > n) break;
        ans = Math.max(ans, nextIdx - i);
      }
      alpDecrease(arr[i] - 'a');
    }
    System.out.println(ans);
  }
  private static void alpIncrease(int alpidx) {
    if (alp[alpidx]++ == 0){
      alpCnt ++;
    }
  }

  private static void alpDecrease(int alpidx) {
    if (alp[alpidx]-- == 1){
      alpCnt --;
    }
  }
}
