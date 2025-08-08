
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int ask[][] = new int[N][3];
    for (int i = 0; i < N; i++) {
      int number = sc.nextInt();
      int strike = sc.nextInt();
      int ball = sc.nextInt();
      ask[i][0] = number;
      ask[i][1] = strike;
      ask[i][2] = ball;
    }
    int ans = 0;
    for (int i = 100; i <= 999; i++) {
      boolean flag = true;
      char[] charI = String.valueOf(i).toCharArray();

      // 같은 숫자 continue
      if (charI[0] == charI[1] || charI[1] == charI[2] || charI[0] == charI[2]) continue;
      if (charI[0] == '0' || charI[1] == '0' || charI[2] == '0') continue;

      for (int j = 0; j < N; j++) {
        int bcnt =0 , scnt = 0;
        char[] charJ = String.valueOf(ask[j][0]).toCharArray();

        for (int k = 0; k < 3; k++) {
          for (int l = 0; l < 3; l++) {
            if (charI[k] == charJ[l]) {
              if (k == l) scnt++;
              else bcnt++;
            }
          }
        }
        if (scnt != ask[j][1] || bcnt != ask[j][2]) {
          flag = false;
          break;
        }
      }
      if (flag) ans++;
    }

    System.out.println(ans);


  }
}
