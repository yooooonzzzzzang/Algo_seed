import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int ans = 0;
    while (n-- > 0) {
      char[] arr = scanner.next().toCharArray();
      // 선 끼리 교차된다. -> 스택과 연관?
      Deque<Character> stack = new ArrayDeque<>();
      for (char c : arr) {
        if(stack.isEmpty()){
          stack.push(c);
        } else {
          if (stack.peek() == c){
            stack.pop();
          }else {
            stack.push(c);
          }
        }
      }
      if (stack.isEmpty()){
        ans += 1;
      }
    }

    System.out.println(ans);
  }
}
