
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  static int getWifiInstallationCnt(int distance, int[]arr){
    int cnt = 1;
    int prev = arr[0];
    for(int i = 1; i < arr.length; i++){
      if(arr[i] - prev >= distance){
        prev = arr[i];
        cnt ++;
      }
    }

    return cnt;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] inputs = br.readLine().split(" ");

    int N = Integer.parseInt(inputs[0]);
    int M = Integer.parseInt(inputs[1]);

    int[] arr = new int[N];

    for (int i = 0; i < N; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }
    Arrays.sort(arr);


    int s = 1;
    int e = arr[N-1] - arr[0];
    int ans = 0;

    while (s <= e) {
      int mid  = (s+e)/2;
      if (getWifiInstallationCnt(mid, arr) >= M) {
        ans = mid;
        s = mid + 1;
      } else {
        e = mid - 1;
      }
    }
    System.out.println(ans);
  }
}
