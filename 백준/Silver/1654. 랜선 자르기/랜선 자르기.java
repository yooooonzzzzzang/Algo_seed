
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  static long cut(long target, long[]arr){
    long result = 0;
    for (long a : arr){
      result += (a/target);
    }
    return result;
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int[] inputs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int K = inputs[0];
    int N = inputs[1];
    long[] lines = new long[K];
    for (int i = 0; i < K; i++) {
      lines[i] = Long.parseLong(br.readLine());
    }

    Arrays.sort(lines);

    long s = 1L;
    long e =  lines[K-1];
    long ans = 1L;

    while (s <= e) {
      long mid = (s + e)/2;
      long cut = cut(mid, lines);
      if (cut >= N){
        s = mid + 1;
        ans = mid;
      } else {
        e = mid - 1;
      }
    }
    System.out.println(ans);
  }

}
