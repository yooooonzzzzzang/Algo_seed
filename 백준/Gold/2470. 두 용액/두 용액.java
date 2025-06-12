
import com.sun.source.tree.BreakTree;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    Arrays.sort(arr);
    int left = 0;
    int right = N - 1;
    int min = Integer.MAX_VALUE;
    int ans1 = 0, ans2 = 0;

    while (left < right) {
      int sum = arr[left] + arr[right];

      if (Math.abs(sum) < min) {
        min = Math.abs(sum);
        ans1 = arr[left];
        ans2 = arr[right];
      }

      if (sum < 0) left++;
      else right--;
    }

    System.out.println(ans1 + " " + ans2);

  }
}
