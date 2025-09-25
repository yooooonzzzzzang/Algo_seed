import java.util.Scanner;

public class Main {
  static int n;
  static int min_ans = Integer.MAX_VALUE;
  static int max_ans = Integer.MIN_VALUE;
  static int[] arr;
  static int[] ops;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    ops = new int[4];
    for (int i = 0; i < 4; i++) {
      ops[i] = sc.nextInt();
    }

    recur(1,arr[0]);
    System.out.println(max_ans);
    System.out.println(min_ans);
  }
  static void recur(int idx, int sum) {
    // -10 보다 작거나 10억보다 크면 return
    if (idx == n) {
      min_ans = Math.min(min_ans, sum);
      max_ans = Math.max(max_ans, sum);
      return;
    }
    // + - * %
    if(ops[0] > 0) {
      ops[0]--;
      recur(idx+1, sum+arr[idx]);
      ops[0]++;
    };
    if(ops[1] > 0) {
      ops[1]--;
      recur(idx+1, sum-arr[idx]);
      ops[1]++;
    };
    if(ops[2] > 0) {
      ops[2]--;
      recur(idx+1, sum*arr[idx]);
      ops[2]++;
    };
    if(ops[3] > 0) {
      ops[3]--;
      recur(idx+1, sum/arr[idx]);
      ops[3]++;
    };
  }
}
