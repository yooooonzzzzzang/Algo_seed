
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
/**
 * 첫째 줄에 테스트 케이스의 개수가 주어진다.
 * 각 테스트 케이스는 한줄로 이루어져 있고,
 * 강산이가 입력한 순서대로 길이가 L인 문자열이 주어진다. (1 ≤ L ≤ 1,000,000)
 * 강산이가 백스페이스를 입력했다면, '-'가 주어진다.
 * 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다.
 * 화살표의 입력은 '<'와 '>'로 주어진다.
 * 이때는 커서의 위치를 움직일 수 있다면,
 * 왼쪽 또는 오른쪽으로 1만큼 움직인다.
 * 나머지 문자는 비밀번호의 일부이다.
 * 물론, 나중에 백스페이스를 통해서 지울 수는 있다.
 * 만약 커서의 위치가 줄의 마지막이 아니라면,
 * 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.
 *
 */

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int T = scanner.nextInt();
    while (T-- > 0) {
      char[] charArray = scanner.next().toCharArray();
      Deque<Character> stack = new ArrayDeque<>();
      Deque<Character> stack2 = new ArrayDeque<>();
      for (int i = 0; i < charArray.length; i++) {
        char c = charArray[i];
        if (c == '<' ) {
          if (!stack.isEmpty()) stack2.offerFirst(stack.pollLast());}
        else if (c == '>' ) {
          if (!stack2.isEmpty()) stack.offerLast(stack2.pollFirst());}
        else if (c =='-'){
          if(!stack.isEmpty())stack.removeLast();
        }
        else{
          stack.offerLast(c);
        }
      }

      StringBuilder sb = new StringBuilder();
      while (!stack.isEmpty()) {sb.append(stack.pollFirst());}
      while (!stack2.isEmpty()) {sb.append(stack2.pollFirst());}
      System.out.println(sb);
    }
  }
}
