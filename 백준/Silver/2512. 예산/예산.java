
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  static int solution(int mid, int[]arr){
    int result =0;
    for(int i=0;i<arr.length;i++){
      if (arr[i] > mid){
        result += mid;
      } else result += arr[i];
    }

    return result;
  }
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(integer -> Integer.parseInt(integer)).sorted().toArray();
    int M = Integer.parseInt(br.readLine());


    int s = 1;
    int e = arr[N-1];
    int ans = 0;
    while (s <= e) {
      int mid = (s+e) / 2;
      if (solution(mid, arr) <= M){
        ans = mid;
        s = mid + 1;
      } else e = mid - 1;
    }

    System.out.println(ans);
  }
}
