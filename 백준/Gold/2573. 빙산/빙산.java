
import java.util.Scanner;

public class Main {

  static int n,m;
  static int[] dx = {-1, 0, 1, 0};
  static int[] dy = {0, 1, 0, -1};
  static int[][] graph;
  static int[][] calGraph;
  static boolean[][] visited;
  static boolean flag;
  static int ans;
  static int countt;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    m = sc.nextInt();
    graph = new int[n][m];


    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        graph[i][j] = sc.nextInt();
      }
    }
    melt();



  }
  static void melt(){
    while (true) {
      visited = new boolean[n][m];
      calGraph = new int[n][m];
      countt = 0;
      ans ++;
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          if (graph[i][j] != 0) {
            int cnt = 0;
            for (int k = 0; k < 4; k++) {
              int ni = i + dx[k];
              int nj = j + dy[k];
              if (ni >= 0 && ni < n && nj >= 0 && nj < m && graph[ni][nj] == 0) {
                cnt++;
              }
            }
            calGraph[i][j] = graph[i][j] - cnt > 0 ? graph[i][j] - cnt : 0;
          }
        }
      }
      // 옮기기
      graph = calGraph;


      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          if (!visited[i][j] && graph[i][j] != 0) {
            countt++;
            dfs(i, j);
          }
        }
      }
      if (countt == 0) {
        System.out.println(0);
        break;
      }
      if (countt >=2){
        System.out.println(ans);
        break;
      }
    }
  }

  static void dfs(int x, int y){
    visited[x][y] = true;
    for (int k = 0; k < 4; k++) {
      int ni = x + dx[k];
      int nj = y + dy[k];
      if (0 <= ni && ni < n && 0 <= nj && nj < m && graph[ni][nj] != 0 && !visited[ni][nj]) {
        dfs(ni,nj);
      }
    }
  }
}
