
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

  public static void main(String[] args) throws IOException {
    /*
    * 스택의 top이 현재 프렛보다 크면 → 손가락 떼기 (pop + 연주 횟수 증가)

스택의 top이 현재 프렛과 같으면 → 아무 일도 안 함

스택이 비었거나 top보다 큰 값이면 → 새로 누르기 (push + 연주 횟수 증가)
    *
    * */
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] s = br.readLine().split(" ");
    int N = Integer.parseInt(s[0]);
    int P = Integer.parseInt(s[1]);

    Deque<Integer>[] stack = new ArrayDeque[7];

    for (int i = 1; i <= 6; i++) {
      stack[i] = new ArrayDeque<>();
    }


    int ans = 0;
    while (N-- > 0) {
      String[] cmds = br.readLine().split(" ");
      int line = Integer.parseInt(cmds[0]);
      int num = Integer.parseInt(cmds[1]);

      while (!stack[line].isEmpty()) {
        if ( stack[line].peek() > num) {
          ans ++;
          stack[line].poll();
        }
        else break;
      }
      if (!stack[line].isEmpty() && stack[line].peek() == num) {continue;}
      // 연주가능
      stack[line].addFirst(num);
      ans ++;
    }

    System.out.println(ans);

  }
}
