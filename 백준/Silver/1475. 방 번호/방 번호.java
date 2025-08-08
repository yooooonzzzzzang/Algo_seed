
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int nums[] = new int[10];
    String strs = sc.next();

    for (int i = 0; i < strs.length(); i++) {
      nums[strs.charAt(i) - '0']++;
    }
    nums[6] += nums[9];
    nums[6] = nums[6] / 2 + nums[6] %2;
    nums[9] = 0;

    System.out.println(Arrays.stream(nums).max().getAsInt());
  }

}
