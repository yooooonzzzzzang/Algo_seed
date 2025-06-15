import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  static int countK(int num, int[] arr){
    int result = 1;
    int now = num;
    for(int i =0;i<arr.length;i++){
      if (now < arr[i]){
        now = num;
        result++;
      }
      now -= arr[i];
    }
    return result;
  }
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] strs = br.readLine().split(" ");
    int N = Integer.parseInt(strs[0]);
    int M = Integer.parseInt(strs[1]);
    int[] arr = new int[N];
    for (int i = 0; i < N; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }

    int s = Arrays.stream(arr).max().getAsInt();
    int e = N * 10000;
    int ans = 1;
    while (s <= e) {
      int mid = ( s + e ) / 2;
      if (countK(mid, arr) <= M) {
        ans = mid;
        e = mid - 1;
      }
      else {
        s = mid + 1;
      }
    }
    System.out.println(ans);
  }
}
