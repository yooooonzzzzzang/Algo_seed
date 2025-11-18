
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  static class Node {
    int x;
    int y;
    int broken;
    Node(int x, int y, int broken) {
      this.x = x;
      this.y = y;
      this.broken = broken;
    }
  }
  static int[] dx = {-1,0,1,0};
  static int[] dy = {0,1,0,-1};
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    char[][] graph = new char[n][m];
    int[][][] v = new int[n][m][2];
    for (int i = 0; i < n; i++) {
      String arg = sc.next();
      for (int j = 0; j < m; j++) {
        graph[i][j] = arg.charAt(j);
      }
    }
    Queue<Node> queue = new LinkedList<>();
    queue.add(new Node(0, 0,0));
    v[0][0][0] = 1;

    boolean isAnswered = false;
    while (!queue.isEmpty()) {
      Node poll = queue.poll();
      int x = poll.x;
      int y = poll.y;
      int broken = poll.broken;
      // 도착
      if (x == n - 1 && y == m - 1) {
        System.out.println(v[x][y][poll.broken]);
        return;
      }
      for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0<=nx && nx < n && 0<=ny && ny < m) {

          if (graph[nx][ny] == '0' && v[nx][ny][broken] == 0){
            v[nx][ny][broken] = v[x][y][broken] + 1;
            queue.add(new Node(nx, ny, broken));
          } else if (graph[nx][ny] == '1' && broken == 0 && v[nx][ny][1] == 0) {
            v[nx][ny][1] = v[x][y][0] + 1;
            queue.add(new Node(nx, ny, 1));
          }
        }
      }
    }
      System.out.println(-1);



  }
}
