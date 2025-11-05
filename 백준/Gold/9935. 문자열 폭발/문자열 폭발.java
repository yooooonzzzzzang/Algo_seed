import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class Main {

  static String str;
  static String compare;
  static Stack<Character> stack = new Stack<>();
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    str = sc.nextLine();
    compare = sc.nextLine();
    int m = compare.length();

    for(int i = 0; i < str.length(); i++){
      stack.push(str.charAt(i));
      if(stack.size()< m){
        continue;
      }
      boolean flag = true;
      // 1 2 3      4123
      for(int j = 0; j < m; j++){
        if(compare.charAt(j) != stack.get(stack.size()-m+j)){
          flag = false;
          break;
        }
      }
      if (flag){
        for (int j = 0; j < m; j++){
          stack.pop();
        }
      }

    }
    if (stack.isEmpty()) {
      System.out.println("FRULA");
    } else {
      StringBuilder sb = new StringBuilder();
      for (int i = 0; i < stack.size(); i++) {
        sb.append(stack.get(i));
      }
      System.out.println(sb.toString());
    }

  }
}
