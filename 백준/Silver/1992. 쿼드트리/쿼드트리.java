
import java.util.Scanner;

public class Main {
  static int n;
  static int[][] arr;
  static String ans;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    arr = new int[n][n];
    for (int i = 0; i < n; i++) {
      String s = sc.next();
      for (int j = 0; j < n; j++) {
        arr[i][j] = s.charAt(j) - '0';
      }
    }

    System.out.println(conquer(0,0,n));

  }
  static String conquer(int x, int y, int size){
    if (size == 1){
      return String.valueOf(arr[x][y]);
    }

    int origin = arr[x][y];
    boolean same = true;

    for (int i = x; i < x+size; i++) {
      for (int j = y; j < y+size; j++) {
        if (arr[i][j] != origin){
          same = false;
          break;
        }
      }
    }

    if (same){return String.valueOf(arr[x][y]);}

    int half = size / 2;
    String topLeft = conquer(x, y, half);
    String topRight = conquer(x, y+half, half);
    String bottomLeft = conquer(x+half, y, half);
    String bottomRight = conquer(x+half, y+half, half);

    return "(" + topLeft + topRight + bottomLeft + bottomRight + ")";
  }
}
