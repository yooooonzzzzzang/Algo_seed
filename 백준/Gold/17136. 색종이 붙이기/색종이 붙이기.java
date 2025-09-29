
import java.util.Scanner;

public class Main {

  static int[][] board = new int[10][10];
  static int[] colors = {0,5,5,5,5,5};
  static int ans = Integer.MAX_VALUE;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        board[i][j] = sc.nextInt();
      }
    }


    recur(0,0,0);
    System.out.println(ans == Integer.MAX_VALUE ? -1 :ans);
  }

  static void recur(int x, int y , int cnt) {
    // base
    if (x == 10) {
      ans = Math.min(ans, cnt);
      return;
    }
    if (cnt >= ans) return;

    if (y==10){
      recur(x+1,0,cnt);
      return;
    }

    if (board[x][y] == 0) {
      recur(x, y+1, cnt);
      return;
    }

    for (int i = 5; i >= 1; i--) {
          if (colors[i] == 0) continue;

          if(canAttach(x, y, i)) {
            attach(x, y, i, 0);
            colors[i]--;
            recur(x, y + 1, cnt + 1);
            attach(x, y, i, 1);
            colors[i]++;
          }

     }
  }

  private static boolean canAttach(int x, int y, int size) {
    if (x+size > 10 || y+size > 10) return false;
    // 범위 내 1 확인
    for (int i = x; i < x+size; i++){
      for (int j = y; j < y+size; j++){
        if (board[i][j] == 0) return false;
      }
    }
    return true;
  }
  static void attach(int x, int y, int size, int val) {
    for (int i = x; i < x+size; i++){
      for (int j = y; j < y+size; j++){
        board[i][j] = val;
      }
    }
  }


}
