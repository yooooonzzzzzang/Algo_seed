
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int Q = scanner.nextInt();
    int[] arr = new int[N+1];
    for (int i = 1; i <= N; i++) {
      arr[i] = scanner.nextInt();
    }

    int[] prefix = new int[N+1];

    for (int i = 1; i <= N; i++) {
      prefix[i] =  prefix[i-1] ^ arr[i] ;
    }
    int ans = 0;
    while (Q-- > 0){
      int s = scanner.nextInt();
      int e = scanner.nextInt();
      ans ^= prefix[e] ^ prefix[s-1];
    }
    System.out.println(ans);
  }
}
