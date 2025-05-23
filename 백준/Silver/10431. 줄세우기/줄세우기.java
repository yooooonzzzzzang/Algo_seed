
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t = Integer.parseInt(br.readLine());
    for (int i = 0; i < t; i++) {
      String[] strs = br.readLine().split(" ");
      int ans = 0;
      int[] numbers = Arrays.stream(Arrays.copyOfRange(strs, 1, strs.length))
          .mapToInt(Integer::parseInt)
          .toArray();

      for (int j = 0; j < 20; j++) {
        int num = numbers[j];
        for (int k = 0; k < j; k++) {
          if (num < numbers[k] && k < j) {
            int numIndex = j ;
            int tempnum = numbers[j];
            for (int l = numIndex; l > k; l--) {
              numbers[l] = numbers[l-1];
              ans +=1;
            }
            numbers[k] = tempnum;
            break;
          }
        }
      }
      System.out.println(strs[0] + " " + ans);
    }
  }

}
