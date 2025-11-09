
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  static int n, m;
  static int[][] arr;
  static int[][] visited;
  static int[] dx= {-1, 0, 1, 0};
  static int[] dy= {0, 1, 0, -1};
  static Queue<Point> queue = new LinkedList<>();
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
    n = sc.nextInt();
    m = sc.nextInt();
    arr = new int[n][m];
    visited = new int[n][m];
    for (int i = 0; i < n; i++) {
      String line = sc.next();
      for (int j = 0; j < m; j++) {
        arr[i][j] = line.charAt(j) - '0';
      }
    }

    System.out.println(bfs(0,0));
  }

  static int bfs(int i, int j) {
    queue.add(new Point(i, j));
    visited[i][j] = 1;
    while (!queue.isEmpty()) {
      Point cur = queue.poll();
      if (cur.x == n-1 && cur.y == m-1) {
        return visited[cur.x][cur.y];
      }
      for (int k = 0; k < 4; k++) {
        int nx = cur.x + dx[k];
        int ny = cur.y + dy[k];
        if (0<=nx && nx < n && 0<=ny && ny < m && visited[nx][ny] ==0 && arr[nx][ny] == 1) {
          queue.add(new Point(nx, ny));
          visited[nx][ny] = visited[cur.x][cur.y] + 1;
        }
      }

    }
    return -1;
  }
}
