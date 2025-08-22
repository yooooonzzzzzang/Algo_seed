
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    int[] arr = new int[N];
    Deque<Integer> stack = new ArrayDeque<>();

    for (int i = 0; i < N; i++) {
      arr[i] = Integer.parseInt(br.readLine());
    }
    StringBuilder sb = new StringBuilder();



    int idx = 0;
    for (int i = 1; i <= N; i++) {
      while (!stack.isEmpty() && stack.peek() == arr[idx]) {
        stack.pop();
        sb.append("-\n");
        idx++;
      }
      stack.push(i);
      sb.append("+\n");
    }
    boolean flag = true;
    while (idx < N){
      if(arr[idx] != stack.peek()){
        flag = false;
        break;
      }
      stack.pop();
      sb.append("-\n");
      idx++;

    }
    if (flag)
      System.out.println(sb);
    else {
      System.out.println("NO");
    }
  }
}
