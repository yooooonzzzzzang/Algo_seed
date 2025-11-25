
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  static int n, m;
  static char[][] arr;
  static int[][][] v;
  static int[] dx = {-1,0,1,0};
  static int[] dy = {0,1,0,-1};

  static class Node {
    int x,y, key;
    public Node(int x, int y, int k) {
      this.x = x;
      this.y = y;
      this.key = k;
    }
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    m = sc.nextInt();
    arr = new char[n][m];
    v = new int[n][m][1<<6];
    Queue<Node> q = new LinkedList<>();

    for (int i = 0; i < n; i++) {
      String next = sc.next();
      for (int j = 0; j < m; j++) {
        arr[i][j] = next.charAt(j);
        if (arr[i][j] == '0') {
          // 현재위치
          q.add(new Node(i, j, 0));
          v[i][j][0] = 1;
        }
      }
    }

    while (!q.isEmpty()) {
      Node cur = q.poll();
      for (int i = 0; i < 4; i++) {
        int nx = cur.x + dx[i];
        int ny = cur.y + dy[i];
        if(isOutOfRange(nx, ny)) continue;
        char next = arr[nx][ny];
        if (next=='#') continue;
        else if (next=='.' || next=='0') {
          if (v[nx][ny][cur.key] == 0){
            v[nx][ny][cur.key] = v[cur.x][cur.y][cur.key]+1;
            q.add(new Node(nx, ny, cur.key));
          }
        }
        else if (next=='1') {
          System.out.println(v[cur.x][cur.y][cur.key]);
          return;
        }
        else if (next >= 'A' && next <= 'F') {
          // 맞는 키가 없다
          if ((cur.key&(1<<(next-'A'))) == 0) continue;
          if (v[nx][ny][cur.key] == 0){
            v[nx][ny][cur.key] = v[cur.x][cur.y][cur.key]+1;
            q.add(new Node(nx, ny, cur.key));
          }
        }
        else if (next >= 'a' && next <= 'f') {
          int nextKey = cur.key | (1<<(next-'a'));
          if (v[nx][ny][nextKey] == 0) {
            v[nx][ny][nextKey] = v[cur.x][cur.y][cur.key]+1;
            q.add(new Node(nx, ny, nextKey));
          }
        }

      }
    }
    System.out.println(-1);
  }
  static boolean isOutOfRange(int r, int c){
    return (r < 0 || r >= n || c < 0 || c >= m);
  }


}
