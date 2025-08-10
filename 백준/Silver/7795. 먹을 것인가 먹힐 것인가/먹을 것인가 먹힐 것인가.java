
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    while (T-- > 0) {
      String[] splits = br.readLine().split(" ");
      int N = Integer.parseInt(splits[0]);
      int M = Integer.parseInt(splits[1]);

      int[] arrN = new int[N];
      int[] arrM = new int[M];
      splits = br.readLine().split(" ");
      for (int i = 0; i < N; i++) {
        arrN[i] = Integer.parseInt(splits[i]);
      }
      splits = br.readLine().split(" ");
      for (int i = 0; i < M; i++) {
        arrM[i] = Integer.parseInt(splits[i]);
      }

      Arrays.sort(arrM);
      int ans = 0;
      ans = getAns(N, M, arrN, arrM, ans);
      System.out.println(ans);


    }
  }

  private static int getAns(int N, int M, int[] arrN, int[] arrM, int ans) {
    for (int i = 0; i < N; i++) {
      int s = 0;
      int e = M;
      int mid=0 ;
      while (s <  e){
        mid = (s + e )/2;
        if (arrN[i] > arrM[mid]){
          s = mid + 1;

        } else{
          e = mid;
        }
      }
      ans += s;
    }
    return ans;
  }
}
