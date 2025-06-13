
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
  static long cut(int target, int[] arr){
    long cnt = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] > target) cnt += (arr[i] - target);
    }
    return cnt;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int[] inputs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int N = inputs[0];
    int M = inputs[1];
    int[] arr =  Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    Arrays.sort(arr);
    int s = 1;
    int e = arr[N-1];
    int ans = 0;
    while (s <= e){
      int mid = (s +e)/2;
      if (cut(mid, arr) >= M) {
        s = mid + 1;
        ans = mid;
      }
      else e = mid - 1;
    }
    // why
    System.out.println(ans);

  }
}
