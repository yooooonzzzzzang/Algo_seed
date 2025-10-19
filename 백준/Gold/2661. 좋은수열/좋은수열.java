
import java.util.Scanner;

public class Main {
  static int N;
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    N = scanner.nextInt();
    recur(0,"");

  }

  public static void recur(int len, String arr) {
    if(len == N) {
        System.out.println(arr);
        System.exit(0);
    }


    for(int i = 1; i <= 3; i++) {
      String newArr = arr+""+i;
      if (check(newArr)) {
        recur(len+1, newArr);
      }
    }
  }

  public static boolean check(String arr) {
    int len = arr.length();
    for (int i = 1; i<=len/2; i++) {
      if (arr.substring(len-i-i, len-i).equals(arr.substring(len-i,len))) {
        return false;
      }
    }
    return true;
  }
}
