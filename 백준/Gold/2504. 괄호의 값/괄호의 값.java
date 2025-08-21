
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    char[] s = sc.next().toCharArray();

    Deque<Character> st = new ArrayDeque<>();
    int ans = 0;
    int mult = 1;

    for (int i = 0; i < s.length; i++) {
      char c = s[i];

      if (c == '(') {
        st.push('(');
        mult *= 2;
      } else if (c == '[') {
        st.push('[');
        mult *= 3;
      } else if (c == ')') {
        // 스택 비었거나 짝이 다르면 실패
        if (st.isEmpty() || st.peek() != '(') { System.out.println(0); return; }
        // 즉시 닫힘이면 더함
        if (i > 0 && s[i - 1] == '(') ans += mult;
        // 해당 괄호 범위 종료 처리
        st.pop();
        mult /= 2;
      } else if (c == ']') {
        if (st.isEmpty() || st.peek() != '[') { System.out.println(0); return; }
        if (i > 0 && s[i - 1] == '[') ans += mult;
        st.pop();
        mult /= 3;
      } else {
        // 허용되지 않는 문자
        System.out.println(0);
        return;
      }
    }

    // 모두 처리 후 스택이 비어야 올바른 괄호열
    System.out.println(st.isEmpty() ? ans : 0);
  }
}
