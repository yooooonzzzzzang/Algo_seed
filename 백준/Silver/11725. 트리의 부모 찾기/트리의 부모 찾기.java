
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  static int n;
  static List<Integer>[] arr;
  static int[] parents;
  static boolean[] check;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    // 배열
    n = sc.nextInt();
    arr = new ArrayList[n+1];
    parents = new int[n+1];
    check = new boolean[n+1];

    // 내부는 arraylist
    for (int i = 0; i < n+1; i++) {
      arr[i] = new ArrayList<>();
    }

    for (int i = 0; i < n-1; i++) {
      int node1 = sc.nextInt();
      int node2 = sc.nextInt();
      arr[node1].add(node2);
      arr[node2].add(node1);
    }
    find(1);
    StringBuilder sb = new StringBuilder();
    for(int i=2;i<=n;i++){
      sb.append(parents[i]);
      sb.append("\n");
    }
    System.out.println(sb);
  }

  static void find(int node){
    check[node] = true;
    for (int i = 0; i < arr[node].size(); i++) {
      int child = arr[node].get(i);
      if(!check[child]){
        parents[child] = node;
        find(child);
      }
    }
  }
}
