
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  static int n, m, k;
  static int[][] arr;
  static int[] dx = {-1,0,1,0};
  static int[] dy = {0,1,0,-1};
  static int[][][] v ;
  static class Node {
    int x, y, broken;

    public Node(int x, int y, int broken) {
      this.x = x;
      this.y = y;
      this.broken = broken;
    }
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    m = sc.nextInt();
    k = sc.nextInt();
    arr = new int[n][m];
    v = new int[n][m][k+1];

    for (int i = 0; i < n; i++) {
      String strs = sc.next();
      for (int j = 0; j < m; j++) {
        arr[i][j] = strs.charAt(j) - '0';
      }
    }
    Queue<Node> q = new LinkedList<>();
    q.add(new Node(0, 0, 0));
    v[0][0][0] = 1;

    while (!q.isEmpty()) {
      Node cur = q.poll();
      int x = cur.x;
      int y = cur.y;
      int broken = cur.broken;
      if (x == n-1 && y == m-1) {
        System.out.println(v[x][y][broken]);
        return;
      }

      for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0<=nx && nx < n && 0<=ny && ny < m) {
          if(v[nx][ny][broken] == 0){
            if(arr[nx][ny] == 0){
              v[nx][ny][broken] = v[x][y][broken]+1;
              q.add(new Node(nx, ny, broken));
            }
            else if (arr[nx][ny] == 1 && broken < k && v[nx][ny][broken + 1]==0){
              v[nx][ny][broken+1] = v[x][y][broken]+1;
              q.add(new Node(nx, ny, broken+1));
            }
          }
        }
      }
    }
    System.out.println(-1);


  }
}
