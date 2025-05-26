
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    char[][] matrix = new char[N][N];
    for (int i = 0; i < N; i++) {
      matrix[i] = br.readLine().toCharArray();  // IntStream 반환
    }

    int ans = 0;

    // 1. 2 방향으로 인접하게 교환 ( 아래, 오른쪽 )
    // 2. 행, 열로 가장 긴 연속 부분 체크해서 갱신
    // 3. 교환 원래대로
    int[] dx = {-1, 0};
    int[] dy = {0, 1};


    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        for (int k = 0; k < 2; k++) {
          char cur = matrix[i][j];
          int nx = i + dx[k];
          int ny = j + dy[k];
          if (nx < 0 || ny < 0 || nx >= N || ny >= N) {
            continue;
          }
          char tmp = matrix[nx][ny];
          matrix[nx][ny] = cur;
          matrix[i][j] = tmp;


          for (int l = 0; l < N; l++) {
            ans = Math.max(longest(matrix[l]),ans);
          }
          for (int c = 0; c < N; c++) {
            char[] colArray = getColumn(matrix, c);
            ans = Math.max(longest(colArray), ans);
          }
          matrix[nx][ny] = tmp;
          matrix[i][j] = cur;
        }
      }
    }
    System.out.println(ans);

  }
  static char[] getColumn(char[][] matrix, int col) {
    int N = matrix.length;
    char[] column = new char[N];
    for (int i = 0; i < N; i++) {
      column[i] = matrix[i][col];
    }
    return column;
  }

  private static int longest(char[] matrix) {
    int ans = 0;
    int tmp = 1;
    for (int i = 1; i < matrix.length; i++) {
      if (matrix[i] != matrix[i - 1]) {ans = Math.max(ans, tmp); tmp = 1; }
      else tmp ++;
    }
    ans = Math.max(ans, tmp);
    return ans;
  }
}
