
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
  static List<Integer>[] tree;
  static int[] counts;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    tree = new List[n + 1];
    counts = new int[n + 1];

    for (int i = 1; i <= n; i++) {
      tree[i] = new ArrayList<>();
      int parent = sc.nextInt();
      if (parent > -1) tree[parent].add(i);
    }

    for (int i = 0; i < m; i++) {
      int person = sc.nextInt();
      int score = sc.nextInt();
      counts[person] += score;
    }
    next(1);
    for(int i = 1; i <= n; i++) {
      System.out.print(counts[i]+" ");
    }


  }

  static void next(int node){
    for (int child : tree[node]){
      counts[child] += counts[node];
      next(child);
    }
  }
}
