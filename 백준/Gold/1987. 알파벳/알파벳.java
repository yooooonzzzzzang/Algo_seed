
import java.util.Scanner;

public class Main {
  static int r, c;
  static int[] alpha;
  static int[][] arr;
  static int ans;
  static int[] dx = {-1, 0, 1, 0};
  static int[] dy = {0, 1, 0, -1};
  // 비트마스크 (row, col) 도달했을때 사용한 알파벳
  static int[][] visited;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    r = sc.nextInt();
    c = sc.nextInt();

    alpha =new int[26];
    arr = new int[r][c];
    visited = new int[r][c];

    for (int i = 0; i < r; i++) {
      String s = sc.next();
      for (int j = 0; j < c; j++) {
        arr[i][j] = s.charAt(j) - 'A';
      }
    }
    visited[0][0] = 1 << (arr[0][0]);
    alpha[arr[0][0]] = 1;
    recur(0, 0, 1);
    System.out.println(ans);
  }

  public static void recur(int x, int y, int cnt) {
    ans = Math.max(ans, cnt);

    for (int d = 0; d < 4; d++) {
      int nx = x + dx[d];
      int ny = y + dy[d];
      if (nx < 0 || ny < 0 || nx >= r || ny >= c)
        continue;
      int next = arr[nx][ny];
      if (alpha[next] != 0)
        continue;
      int route = 1 << next;
      if (visited[nx][ny] == (visited[x][y] | route))
        continue;

      visited[nx][ny] = visited[x][y] | route;
      alpha[arr[nx][ny]]++;
      recur(nx, ny, cnt + 1);
      alpha[arr[nx][ny]]--;

    }
  }

}
