
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.stream.Collectors;

public class Main {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    ArrayList<Integer> ans = new ArrayList();
    int N = Integer.parseInt(br.readLine());
    Queue<Integer> queue = new LinkedList<>();
    int command;
    while ((command = Integer.parseInt(br.readLine())) != -1) {
      if(command == 0) queue.poll();
      else {
        if (queue.size() < N) {
          queue.offer(command);
        }
      }
    }

    System.out.println(queue.size() == 0 ? "empty" :
        queue.stream()
            .map(String::valueOf)
            .collect(Collectors.joining(" "))
    );
  }
}
