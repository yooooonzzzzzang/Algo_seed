
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
  static int solution(int[]arr, int mid){
    int res = 0;

    for(int i=0;i<arr.length;i++){
      int did = arr[i] % mid;
      int mok = arr[i] / mid;
      if (did > 0 ){res ++;}
      res += mok;
    }
    return res;
  }
  public static void main(String[] args) throws IOException {
    // 기준이 질투심
    //  N명의 학생들에게 나누어 주려고 한다. 이때, 보석을 받지 못하는 학생이 있어도 된다.
    //  하지만, 학생은 항상 같은 색상의 보석만 가져간다.
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] s1 = br.readLine().split(" ");
    int N = Integer.parseInt(s1[0]);
    int M = Integer.parseInt(s1[1]);
    int[] arr = new int[M];
    for (int i = 0; i < M; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }
    Arrays.sort(arr);

    int s = 1;
    int e = arr[M-1];
    int ans = 0;
    while (s <= e){
      // 최대값
      int mid = (s + e) / 2;
      // 나눠줄수있는학생이 학생보다 작다 == 너무 많이 나눠준다 mid 를 줄여야함
      if (solution(arr, mid) <= N){
        ans = mid;
        e = mid - 1;
      } else {
        // 나눠줄수있는학생이 학생보다 크다 == 높여야함
        s = mid + 1;
      }
    }
    System.out.println(ans);
  }
}
