import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int b = sc.nextInt();
    int [] broken = new int[n+1];
    // 고장 났으면 1
    for (int i = 0; i < b; i++) {
      broken[sc.nextInt()] = 1;
    }
    int curr = 0;
    for (int i = 1; i <= k; i++) {
      if (broken[i] == 1) curr++;
    }

    int ans = curr;
    // 길이가 k 인 윈도우를 옮기며 1이 최소인 카메라 수를 센다
    for (int i = k+1; i<= n; i++){
      if (broken[i] == 1) curr++;
      if (broken[i-k] == 1) curr --;
      ans = Math.min(ans, curr);
    }
    System.out.println(ans);

  }
}
