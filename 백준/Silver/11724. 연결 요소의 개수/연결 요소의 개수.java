import java.util.ArrayList;
import java.util.Scanner;

public class Main {
  static int n, m ;
  static ArrayList<Integer>[] graph;
  static boolean[] visited;
  static boolean flag = false;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    m = sc.nextInt();

    graph = new ArrayList[n+1];
    for (int i = 1; i <= n ; i++) {
      graph[i] = new ArrayList<>();
    }
    visited = new boolean[n+1];
    for (int i = 0; i < m; i++) {
      int v1 = sc.nextInt();
      int v2 = sc.nextInt();
      graph[v1].add(v2);
      graph[v2].add(v1);
    }
    int ans = 0;

    for (int i = 1; i <= n ; i++) {
      flag = false;
      dfs(i);
      if (flag){
        ans ++;
      }
    }
    System.out.println(ans);


  }
  static void dfs(int v){
     if(!visited[v]) {
      visited[v] = true;
      flag = true;
    }
    for (int next : graph[v]) {
      if (!visited[next]) {
        flag = true;
        visited[next] = true;
        dfs(next);
      }
    }
  }
}
