
import java.util.Scanner;

public class Main {
  static int[][] getPrefixSum(char[][]arr, int n, int m){
    int[][] res = new int[n+1][m+1];
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        res[i][j] = res[i-1][j] + res[i][j-1] - res[i-1][j-1] + (arr[i][j]=='*'? 1:0);
      }
    }
    return res;
  }

  static int getAroundCnt(int r, int c, int k, int[][] acc, int n, int m){
    int r1 = Math.max(r-k,1);
    int c1 = Math.max(c-k,1);
    int r2 = Math.min(r+k,n);
    int c2 = Math.min(c+k,m);

    return acc[r2][c2] - acc[r1-1][c2] - acc[r2][c1-1] + acc[r1-1][c1-1] ;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int t = sc.nextInt();
    int k = sc.nextInt();
    int a = sc.nextInt();
    int b = sc.nextInt();
    char[][] arr = new char[n+1][m+1];

    for (int i = 1; i < n+1; i++) {
      String s = sc.next();
      for (int j = 1; j < m+1; j++) {
        arr[i][j] = s.charAt(j-1);
      }
    }

    while (t-- > 0){
      int[][] acc = getPrefixSum(arr, n, m);
      for (int i = 1; i < n+1; i++) {
        for (int j = 1; j < m+1; j++) {
          int aroundCnt = getAroundCnt(i,j, k, acc, n,m);
          if (arr[i][j] == '*'){
            aroundCnt--;
            if (aroundCnt < a || aroundCnt > b) arr[i][j] = '.';
          }
          else if (aroundCnt > a && aroundCnt <= b) arr[i][j] = '*';
        }
      }
    }

    for (int i = 1; i < n+1; i++) {
      for (int j = 1; j < m+1; j++) {
        System.out.print(arr[i][j]);
      }
      System.out.println();
    }

  }

}
