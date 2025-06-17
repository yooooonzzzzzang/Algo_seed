import java.util.Scanner;

public class Main {
  static boolean solution(int[]arr, int target, int m){
    int cnt = 1;
    int now = arr[0];
    for(int i=1;i<arr.length;i++){
      // 강의가 블루레이 target 보다 크면 안된다
        if (target < arr[i]) return false;
        if (arr[i] + now <= target){
          now += arr[i];
        } else {
          now = arr[i];
          cnt ++;
        }
    }
    if (cnt <= m)
      return true;
    return false;
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();

    int[] arr = new int[n];
    for(int i=0;i<n;i++){
      arr[i] = sc.nextInt();
    }

    int s = 1, e = 10000 * 100000, ans = 1;

    while(s<=e){
      int mid = (s + e)/2;
      // 최소 강의로 자른다
      if (solution(arr, mid, m)){
        // 가능하면  더 줄여봐?
        ans = mid;
        e = mid - 1;
      } else s = mid + 1;
    }
    System.out.println(ans);
  }
}
