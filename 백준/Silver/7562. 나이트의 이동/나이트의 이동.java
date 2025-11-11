
import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
  static class Point{
    int x;
    int y;

    public Point(int x, int y) {
      this.x = x;
      this.y = y;
    }
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int[] dx = {-2, -2 , -1, 1, 2, 2, 1, -1};
    int[] dy = {-1, 1, 2, 2, 1, -1, -2, -2};
    while (t-- > 0) {
      int n = sc.nextInt();
      int sX = sc.nextInt();
      int sY = sc.nextInt();
      int eX = sc.nextInt();
      int eY = sc.nextInt();
      int[][] graph = new int[n][n];
      int[][] visit = new int[n][n];
      Deque<Point> queue = new ArrayDeque<>();
      queue.add(new Point(sX,sY));
      visit[sX][sY] = 1;
      while (!queue.isEmpty()) {
        Point point = queue.poll();
        int x = point.x;
        int y = point.y;
        if (x == eX && y == eY) {
          System.out.println(visit[x][y]-1);
          break;
        }
        for (int k = 0; k < 8; k++) {
          int nx = x + dx[k];
          int ny = y + dy[k];
          if (0<= nx && nx < n && 0<= ny && ny < n && visit[nx][ny] == 0) {
            visit[nx][ny] = visit[x][y] + 1;
            queue.add(new Point(nx,ny));
          }
        }

      }
    }
  }
}
