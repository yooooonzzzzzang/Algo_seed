
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int M = scanner.nextInt();
    String[] S = new String[N];
    for (int i = 0; i < N; i++) {
      S[i] = scanner.next();
    }
    Arrays.sort(S);

    int ans = 0;
    for (int i = 0; i < M; i++) {
      String target = scanner.next();

      int s = 0;
      int e = N-1;
      boolean flag = false;

      while (s <= e){
        int mid = (s + e)/2;
        if (S[mid].equals(target)){flag=true;break;}
        // 내가 작으면 음수 -> target 크다 s =
        if (S[mid].compareTo(target) < 0 ){s = mid+1;}
        else e = mid-1;
      }
      if (flag) ans++;
    }
    System.out.println(ans);
  }
}
