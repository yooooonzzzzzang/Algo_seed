
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  static boolean[][] visited;
  static char[][] matrix;
  static int[] dx = {0,1,0,-1};
  static int[] dy = {1,0,-1,0};
  static int n,m;


  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    n = scanner.nextInt();
    m = scanner.nextInt();
    scanner.nextLine();

    matrix = new char[n][m];
    visited = new boolean[n][m];
    for (int i = 0; i < n; i++) {
      String line = scanner.nextLine();
      for (int j = 0; j < m; j++) {
        matrix[i][j] = line.charAt(j);
      }
    }

    int result = bfs(0,0);
    System.out.println(result);
  }

  static class Node{
    int x, y, dist;

    public Node(int x, int y, int dist) {
      this.x = x;
      this.y = y;
      this.dist = dist;
    }
  }

  private static int bfs(int x, int y) {
    Queue<Node> q = new LinkedList<>();
    q.add(new Node(x, y,0));
    visited[x][y] = true;

    while (!q.isEmpty()){
      Node cur = q.poll();

      if (matrix[cur.x][cur.y] == 'C'){
        return cur.dist;
      }
      for(int d = 0; d < 4; d++){
        int nx = cur.x + dx[d];
        int ny = cur.y + dy[d];

        if (0<=nx && nx < n && 0<=ny && ny < m && !visited[nx][ny] && matrix[nx][ny] != '*'){
          q.add(new Node(nx,ny, cur.dist+1));
          visited[nx][ny] = true;

        }
      }
    }

    return -1;
  }

}
