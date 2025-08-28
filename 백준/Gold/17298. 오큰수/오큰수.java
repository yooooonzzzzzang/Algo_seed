
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    // split 대신 StringTokenizer 사용 (빠름)
    StringTokenizer st = new StringTokenizer(br.readLine());
    String[] input = new String[N];
    for (int i = 0; i < N; i++) input[i] = st.nextToken();

    int[] ans = new int[N];
    Deque<Integer> stack = new ArrayDeque<>();

    // === 아래 로직은 기존 알고리즘 그대로 ===
    for (int i = N - 1; i >= 0; i--) {
      int num = Integer.parseInt(input[i]);
      boolean flag = false;
      while (!flag) {
        if (!stack.isEmpty() && stack.peek() > num) {
          ans[i] = stack.peek();
          stack.addFirst(num);
          flag = true;
        } else if (!stack.isEmpty() && stack.peek() <= num) {
          stack.pop();
        } else {
          stack.addFirst(num);
          ans[i] = -1;
          flag = true;
        }
      }
    }

    // 루프 내 print 대신 StringBuilder로 한 번에 출력 (빠름)
    StringBuilder sb = new StringBuilder();
    for (int x : ans) sb.append(x).append(' ');
    System.out.print(sb);
  }
}
