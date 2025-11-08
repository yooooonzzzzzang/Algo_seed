
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
  static int n;
  static List<Node>[] tree;
  static boolean[]visit;
  static int maxDepth =0;
  // 임의
  static int maxV = 1;
  static class Node{
    int v;
    int w;
    Node(int v, int w){
      this.v = v;
      this.w = w;
    }

    @Override
    public String toString() {
      return "Node{" +
          "v=" + v +
          ", w=" + w +
          '}';
    }
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    tree = new ArrayList[n+1];
    for (int i = 1; i <= n; i++) {
      tree[i] = new ArrayList<>();
    }

    for (int i = 0; i < n; i++) {
      int v = sc.nextInt();
      while (true) {
        int next = sc.nextInt();
        if (next == -1) break;
        int dist = sc.nextInt();
        Node node = new Node(next, dist);
        tree[v].add(node);
      }
    }

    int ans = 0;
    visit = new boolean[n+1];
    visit[1] = true;
    dfs(1, 0);
    visit = new boolean[n+1];
    visit[maxV] = true;
    dfs(maxV, 0);
    System.out.println(maxDepth);
  }
  static void dfs(int i, int total) {
    if (total > maxDepth){
      maxDepth = total;
      maxV = i;
    }
    for (Node node : tree[i]) {
      if (!visit[node.v] ) {
        visit[node.v] = true;
        dfs(node.v, total+node.w);
      }
    }
  }
}
