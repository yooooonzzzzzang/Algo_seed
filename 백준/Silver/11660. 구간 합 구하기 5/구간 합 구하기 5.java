
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int M = sc.nextInt();
    int[][] arr = new int[N+1][N+1];
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        arr[i][j] = sc.nextInt();
      }
    }

    // prefix
    int[][] prefix = new int[N+1][N+1];
    prefix[1][1] = arr[1][1];
    for (int i = 1; i <= N; i++) {
      for (int j = 1; j <= N; j++) {
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]+ arr[i][j];
      }
    }
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    while (M-- > 0) {
      int x1 = sc.nextInt();
      int y1 = sc.nextInt();
      int x2 = sc.nextInt();
      int y2 = sc.nextInt();

      int ans = 0;
      ans = prefix[x2][y2] - (prefix[x1-1][y2] + prefix[x2][y1-1]) + prefix[x1-1][y1-1];
      bw.write(ans + "\n");
    }
    bw.flush();
  }
}
