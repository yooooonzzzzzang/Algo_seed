import java.util.Scanner;
import java.util.*;
public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    int n = sc.nextInt();
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    int m = sc.nextInt();
    int[] arr2 = new int[m];
    for (int i = 0; i < m; i++) {
      arr2[i] = sc.nextInt();
    }

    List<Integer> subA = new ArrayList<>();
    List<Integer> subB = new ArrayList<>();

    for (int i = 0; i < n; i++) {
      int sum = 0;
      for (int j = i; j < n; j++) {
        sum += arr[j];
        subA.add(sum);
      }
    }

    for (int i = 0; i < m; i++) {
      int sum = 0;
      for (int j = i; j < m; j++) {
        sum += arr2[j];
        subB.add(sum);
      }
    }

    Collections.sort(subB);
    long count = 0;
    for (int x : subA) {
      int target = t - x;
      // subB에서 target의 개수를 이분탐색으로 구함
      int lower = lowerBound(subB, target);
      int upper = upperBound(subB, target);
      count += (upper - lower);
    }

    System.out.println(count);
  }
  //"target 값 이상이 처음 나타나는 위치
  static int lowerBound(List<Integer> list, int target) {
    int left = 0, right = list.size();
    while (left < right) {
      int mid = (left + right) / 2;
      if (list.get(mid) < target) left = mid + 1;
      else right = mid;
    }
    return left;
  }
  //"target 값을 초과하는 값이 처음 나타나는 위치
  static int upperBound(List<Integer> list, int target) {
    int left = 0, right = list.size();
    while (left < right) {
      int mid = (left + right) / 2;
      if (list.get(mid) <= target) left = mid + 1;
      else right = mid;
    }
    return left;
  }

}
