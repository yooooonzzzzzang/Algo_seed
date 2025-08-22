import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Queue;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    char[] charArray = scanner.nextLine().toCharArray();
    char[] stack = new char[charArray.length];
    int idx = 0;
    for (char c : charArray) {
      stack[idx++] = c;
      // p p a p
      // -3 -2 idx-1  idx
      if (idx >= 4 && stack[idx - 4] == 'P' && stack[idx - 3] == 'P' && stack[idx - 2] == 'A'
          && stack[idx-1] == 'P') {
        idx -= 3;
      }
    }
    System.out.println(idx == 1 && stack[0] =='P'? "PPAP":"NP");
  }

}
