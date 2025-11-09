
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Main {
  static class Subin{
    int position;
    int time;

    public Subin(int position, int time) {
      this.position = position;
      this.time = time;
    }
  }


  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int[] v = new int[100001];
    Queue<Subin> queue = new ArrayDeque<>();
    queue.add(new Subin(n,0));
    v[n] = 1;


    while(!queue.isEmpty()){
      Subin sub = queue.poll();
      int position = sub.position;
      int time = sub.time;
      if (n >= m) {
        System.out.println(n-m);
        break;
      }
      if (position == m) {
        System.out.println(time);
        break;
      }
      if (position + 1 <=100000 && position >=0 && v[position+1] == 0){
        queue.add(new Subin(position+1,time+1));
        v[position+1]++;
      }
      if (position - 1 <=100000 && position -1  >=0 && v[position-1] == 0){
        queue.add(new Subin(position-1,time+1));
        v[position-1]++;
      }
      if (position * 2 <=100000 && position >=0 && v[position*2] == 0){
        queue.add(new Subin(position*2,time+1));
        v[position*2]++;
      }
    }
  }
}
