import java.util.Scanner;

public class Main {
  static int N, d;
  static int[] used;
  static int[] pick;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    N = sc.nextInt();   // minYear
    d = sc.nextInt();   // m
    used = new int[d];
    pick = new int[d];

    dfs(0);
    System.out.println(-1); // 없으면 -1
  }

  // 순열 생성 
  private static void dfs(int depth){
    if (depth == d){
      // 앞자리가 0이면 무효
      if (pick[0] == 0) return;

      // d진수 -> 10진수로 변환해 바로 N과 비교
      int val = convertBaseDToDecimal(pick, d);
      if (val > N){
        System.out.println(val);
        System.exit(0);
      }
      return;
    }

    for (int digit = 0; digit < d; digit++){
      if (depth == 0 && digit == 0) continue; // 선행 0 금지
      if (used[digit] == 0){
        used[digit] = 1;
        pick[depth] = digit;
        dfs(depth + 1);
        used[digit] = 0;
      }
    }
  }


  private static int convertBaseDToDecimal(int[] digits, int base){
    int res = 0;
    for (int i = 0; i < digits.length; i++){
      res = res * base + digits[i];
    }
    return res;
  }
}
