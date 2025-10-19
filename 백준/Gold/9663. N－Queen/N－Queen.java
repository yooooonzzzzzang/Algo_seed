
import java.util.Scanner;

public class Main {
  static int ans = 0;
  static int[] queen = new int[15];
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    System.out.println(solve(N, 0));
  }

  static int solve(int n, int row) {
    int count = 0;
    //base case
    if (row == n) return 1;

    // recursive case
    for (int col = 0; col < n; col++) {
      if (isValid(row, col)) {
        queen[row] = col;
        count += solve(n, row + 1);
      }
    }

    return count;
  }

  static boolean isValid(int row, int col) {
    // 이미 배치된 퀸과 충돌확인
    for (int i=0; i<row; i++){
      if(queen[i] == col) return false;
      // 두 퀸의 행차이와 열차이 절대값이 같으면 대각선이다.
      if(Math.abs(row - i) == Math.abs(col - queen[i])) return  false;
    }
    return true;
  }
}
