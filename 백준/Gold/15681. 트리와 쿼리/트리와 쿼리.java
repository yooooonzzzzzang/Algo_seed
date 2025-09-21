import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  static List<Integer>[] tree;
  static int[] subtree;
  static boolean[] check;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int r = sc.nextInt();
    int q = sc.nextInt();

    tree = new List[n + 1];
    subtree = new int[n + 1];
    check = new boolean[n + 1];

    // 내부는 arraylist
    for (int i = 0; i < n+1; i++) {
      tree[i] = new ArrayList<>();
    }

    for (int i = 0; i < n-1; i++) {
      int node1 = sc.nextInt();
      int node2 = sc.nextInt();
      tree[node1].add(node2);
      tree[node2].add(node1);
    }

    dfs(r);
    for (int i = 1; i <= q; i++) {
      System.out.println(subtree[sc.nextInt()]);
    }

  }
  static void dfs(int node) {
    check[node] = true;
    subtree[node] = 1;

    for (int child : tree[node]){
      if(!check[child]){
        dfs(child);
        subtree[node] += subtree[child];
      }
    }
  }


}
