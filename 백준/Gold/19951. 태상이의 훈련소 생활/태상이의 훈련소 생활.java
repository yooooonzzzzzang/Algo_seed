import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] s = br.readLine().split(" ");
    int N = Integer.parseInt(s[0]);
    int M = Integer.parseInt(s[1]);
    int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    int[]delta = new int[N+2];
    int[]prefix = new int[N+1];
    while (M -- > 0){
      String[] s1 = br.readLine().split(" ");
      int a = Integer.parseInt(s1[0]);
      int b = Integer.parseInt(s1[1]);
      int k = Integer.parseInt(s1[2]);

      delta[a] += k;
      delta[b+1] -= k;

  
    }
    for (int i = 1; i <= N; i++){
        prefix[i] = delta[i] + prefix[i-1];
    }
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


    for (int i = 0; i < N; i++) {
      bw.write(arr[i] + prefix[i+1] +" ");
    }
    bw.flush();
  }
}
