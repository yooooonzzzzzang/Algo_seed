import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int s1 =scanner.nextInt();
    int s2 =scanner.nextInt();
    int s3 =scanner.nextInt();
    int []cntArr = new int[101];
    for (int i = 1; i <= s1; i++) {
      for (int j = 1; j <= s2; j++) {
        for (int k = 1; k <= s3; k++) {
          cntArr[i+j+k] += 1;
        }
      }
    }
    int maxIdx = 0;
    int maxCnt = cntArr[0];
    for (int i = 1; i <= 100; i++) {
      if (cntArr[i] > maxCnt) {
        maxIdx = i;
        maxCnt = cntArr[i];
      }
    }
    System.out.println(maxIdx);
  }
}
