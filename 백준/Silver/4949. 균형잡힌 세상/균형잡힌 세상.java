
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    while (true){
      String s = br.readLine();
      if(s.equals(".")) break;

      char[] arr = s.toCharArray();
      Deque<Character> stack = new ArrayDeque<>();
      boolean isValid = true;
      for(char c : arr){
        if(c == '(' | c == '['){
          stack.push(c);
        } else if (c == ')'){
          if(stack.isEmpty()){isValid = false;break;}
          if(stack.pop() != '(') {isValid = false;break;}
        } else if (c == ']'){
          if(stack.isEmpty()){isValid = false;break;}
          if(stack.pop() != '[') {isValid = false;break;}
        }
      }
      if (!stack.isEmpty()) isValid = false;
      System.out.println(isValid? "yes" : "no");
    }
  }
}
