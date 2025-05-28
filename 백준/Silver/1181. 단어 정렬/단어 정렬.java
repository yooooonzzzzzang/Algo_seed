
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());


    String[] arr = new String[N];
    for (int i = 0; i < N; i++) {
      arr[i] = br.readLine();
    }
    String[] array = Arrays.stream(arr)
        .distinct()
        .sorted(Comparator
            .comparingInt(String::length)
            .thenComparing(Comparator.naturalOrder()))
        .toArray(String[]::new);
    for (int i = 0; i < array.length; i++) {
      System.out.println(array[i]);
    }

  }
}
