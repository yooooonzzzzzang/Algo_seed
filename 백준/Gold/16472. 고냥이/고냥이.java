import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    char[] arr = sc.next().toCharArray();
    int[] alp = new int[27];
    int ans = 0;
    int nextIdx = 0;
    for (int i = 0; i < arr.length; i++) {
      while (nextIdx < arr.length ){
        alp[arr[nextIdx++] - 'a']++;
        if (countAlp(alp) > n) break;
        ans = Math.max(ans, nextIdx - i);
//        System.out.println(i +" " + n extIdx);
      }
      alp[arr[i] - 'a'] --;
    }
    System.out.println(ans);
  }

  private static int countAlp(int[] alp) {
    int cnt =0;
    for (int i = 0; i < 26; i++) {
      if (alp[i] > 0) cnt++;
    }
    return cnt;
  }
}
