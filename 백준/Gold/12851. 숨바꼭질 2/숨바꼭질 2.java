
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int[] v = new int[100001];
    int[] cnt = new int[100001];
    Queue<Integer> queue = new ArrayDeque<>();
    queue.add(n);
    v[n] = 1;
    cnt[n] = 1;

    while(!queue.isEmpty()){
      int now = queue.poll();
      if (now == m) {
        break;
      }
      int[] next = {now + 1, now - 1, now * 2};
      for (int i = 0; i < 3; i++) {
        if(next[i] <= 100000 && next[i] >= 0 ){
          if (v[next[i]] == 0){
            v[next[i]] = v[now]+1;
            cnt[next[i]] = cnt[now];
            queue.add(next[i]);
          } else if (v[next[i]] == v[now]+1){
            cnt[next[i]] += cnt[now] ;
          }
        }
      }
    }
    System.out.println(v[m]-1);
    System.out.println(cnt[m]);
  }
}
