import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  static class Document{
    int index;
    int priority;

    public Document(int index, int priority) {
      this.index = index;
      this.priority = priority;
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    while(T-->0){
      int N = sc.nextInt();
      int M = sc.nextInt();
      Integer[] priorityArr = new Integer[N];
      Queue<Document> queue = new LinkedList<>();

      for(int i = 0; i < N; i++){
        int priority = sc.nextInt();
        queue.add(new Document(i,priority));
        priorityArr[i] = priority;
      }
      // priority reverse sorting
      Arrays.sort(priorityArr, Collections.reverseOrder());

      for (int i = 0; i < N; i++) {
        while(queue.peek().priority != priorityArr[i]){
          queue.offer(queue.poll());
        }
        // 큐 앞 문서가 M index 문서면 인쇄 순서 출력 후 종료
        if(queue.peek().index == M) {
          System.out.println(i + 1);
          break;
        }
        queue.poll();
      }
    }

  }
}



