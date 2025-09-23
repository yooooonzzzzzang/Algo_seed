
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static int l, c;
  static char[] arr;
  static char[] temp;
  static boolean[] v;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    l = sc.nextInt();
    c = sc.nextInt();

    arr = new char[c];
    temp = new char[l];
    v = new boolean[c];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = sc.next().charAt(0);
    }
    Arrays.sort(arr);
    recur(0, 0);
  }
  static void recur(int dept, int start){
    if(dept == l){
      // aeiou cnt
      int cnt =0;
      for (int i = 0; i < l; i++) {
        char c = temp[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
      }
      if(cnt >= 1 && l-cnt >= 2)
        System.out.println(new StringBuilder().append(temp).toString());
      return;
    }
    for (int i=start; i<c; i++){
      if (!v[i]) {
        v[i] = true;
        temp[dept] = arr[i];
        recur(dept+1,i+1);
        v[i] =false;
      }
    }
  }
}
