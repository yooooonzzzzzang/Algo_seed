
import java.util.Scanner;

public class Main {
  static int r, c;
  static int[] alpha;
  static char[][] arr;
  static int ans;
  static int[] dx = {-1, 0, 1, 0};
  static int[] dy = {0, 1, 0, -1};
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    r = sc.nextInt();
    c = sc.nextInt();

    alpha =new int[26];
    arr = new char[r][c];
    sc.nextLine();
    for (int i = 0; i < r; i++) {
      String s = sc.nextLine();
      for (int j = 0; j < c; j++) {
        arr[i][j] = s.charAt(j);
      }
    }
    alpha[arr[0][0] - 'A'] = 1;
    recur(0, 0, 1);
    System.out.println(ans);
  }

  public static void recur(int x, int y, int cnt){
    ans = Math.max(ans, cnt);

    for (int d = 0; d < 4; d++) {
      int nx = x + dx[d];
      int ny = y + dy[d];
      if (nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
      if (alpha [arr[nx][ny]-'A'] == 0){
        alpha [arr[nx][ny]-'A']++;
        recur(nx, ny, cnt +1);
        alpha[arr[nx][ny]-'A']--;
      }
    }
  }
}
