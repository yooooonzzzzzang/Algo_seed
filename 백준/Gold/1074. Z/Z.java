import java.util.Scanner;

public class Main {
  static int n, r, c;
  static int ans = 0;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    r = sc.nextInt();
    c = sc.nextInt();
    conquer(n, r, c);
    System.out.println(ans);
  }
  static void conquer(int n, int r, int c){
    int boardSize = 1 << n; // 2^n
    int mid = boardSize / 2;
    if (n == 0) return;

    // 1
    if (r<mid && c<mid) { conquer(n-1, r, c);}
    // 2
    else if (r<mid && c>=mid) {
      ans += mid * mid;
      conquer(n-1, r, c-mid);
    }
    // 3
    else if (r>=mid && c < mid) {
      ans += mid * mid * 2;
      conquer(n-1, r-mid, c);
    }
    else {
      ans += mid * mid * 3;
      conquer(n-1, r-mid, c-mid);
    }
  }
}
