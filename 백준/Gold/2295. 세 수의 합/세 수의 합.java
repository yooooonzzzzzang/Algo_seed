
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    Integer[] arr = new Integer[N];
    for (int i = 0; i < N; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }
    Arrays.sort(arr);

    Integer[] sums = new Integer[N* (N+1)/2];
    int index = 0;
    // a + b = x - c
    for (int i = 0; i < N; i++) {
      for (int j = i; j < N; j++) {
        sums[index++] = arr[j]+arr[i];
      }
    }
    Arrays.sort(sums);
    int ans = -1;
    for (int i =0 ; i < N; i++){
      for (int j = 0; j < N; j++){
        int target = arr[i] - arr[j];
        if (isExist(sums, target)){
          ans = Math.max(ans,arr[i]);
        }
      }
    }
    System.out.println(ans);
  }

  private static boolean isExist(Integer[] sums, int target) {
    int s = 0;
    int e = sums.length-1;
    while (s <= e){
      int mid = (s+e)/2;
      if (sums[mid] == target){
        return true;
      } else if (sums[mid] > target){
        e = mid-1;
      } else s = mid+1;
    }
    return false;
  }
}
