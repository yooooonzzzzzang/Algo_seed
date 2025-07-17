
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    // max black min white
    int black = sc.nextInt();
    int white = sc.nextInt();
    char[] board = sc.next().toCharArray();

    int bcnt = 0, wcnt = 0, ans = 0;
    int nextIdx = 0;

    for (int i = 0; i < n; i++) {
      while (nextIdx < n){
        if (board[nextIdx] == 'B' && bcnt == black)break;
        if (board[nextIdx++] == 'W' ) wcnt ++;
        else bcnt ++;
      }
      if (wcnt >= white) ans = Math.max(ans, nextIdx-i);
      if (board[i] == 'B') bcnt --;
      else wcnt --;
    }
    System.out.println(ans);
  }
}
