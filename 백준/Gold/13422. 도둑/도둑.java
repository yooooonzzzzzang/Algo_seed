
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    while (T-- > 0) {
      int N = sc.nextInt();
      int M = sc.nextInt();
      int K = sc.nextInt();

      int[] arr = new int[2 * N];
      for (int i = 0; i < N; i++) {
        arr[i] = sc.nextInt();
        arr[i + N] = arr[i]; // 원형 배열 구현
      }

      int ans = 0;
      int curr = 0;

      // 초기 윈도우
      for (int i = 0; i < M; i++) {
        curr += arr[i];
      }
      if (curr < K) ans++;

      // 윈도우 슬라이딩 (N == M이면 딱 한 번만 검사)
      if (N != M) {
          // 초기 윈도우 제외 -1
        for (int i = M; i < N + M -1; i++) {
          curr += arr[i];
          curr -= arr[i - M];
          if (curr < K) ans++;
        }
      }

      System.out.println(ans);
    }
  }
}
