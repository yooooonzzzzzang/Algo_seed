
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int d = sc.nextInt();
    int k = sc.nextInt();
    int c = sc.nextInt();

    int[] dish = new int[N];
    for (int i = 0; i < N; i++) {
      dish[i] = sc.nextInt();
    }

    int[]dishCount = new int[d+1];
    int uniCount = 0;

    // sliding Window Initializing
    for (int i = 0; i < k-1; i++) {
      if (dishCount[dish[i]]++ == 0) uniCount ++;
    }

    // sliding window
    int ans = uniCount;
    for (int i = 0; i < N; i++) {
      if (dishCount[dish[(i+k-1) % N]]++ == 0) uniCount ++;
      ans = Math.max(ans, uniCount + (dishCount[c] == 0 ? 1 : 0));
      if(--dishCount[dish[i]] == 0) uniCount --;
    }

    System.out.println(ans);



  }
}
