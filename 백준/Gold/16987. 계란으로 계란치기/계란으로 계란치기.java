
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
  static int n;
  static List<Egg> eggs;
  static int ans = 0;
  static class Egg{
    public int weight;
    public int durable;

    public Egg(int weight, int durable) {
      this.weight = weight;
      this.durable = durable;
    }

    public void fight(Egg other){
      this.durable -= other.weight;
      other.durable -= this.weight;
    }

    public void restore(Egg other){
      this.durable += other.weight;
      other.durable += this.weight;
    }

  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    eggs = new ArrayList<>(n);
    for (int i = 0; i < n; i++) {
      int durable = sc.nextInt();
      int weight = sc.nextInt();
      eggs.add(new Egg(weight, durable));
    }
    recur(0,0);
    System.out.println(ans);

  }

  static void recur(int now, int cnt){
    if (now == n){
      ans = Math.max(ans, cnt);
      return;
    }

    boolean flag = false;
    if(eggs.get(now).durable > 0){

      for (int i = 0; i < n; i++) {
        if ( i == now || eggs.get(i).durable <= 0) continue;
        flag = true;
        eggs.get(now).fight(eggs.get(i));
        recur(now+1, cnt + (eggs.get(now).durable <= 0 ? 1: 0) + (eggs.get(i).durable <= 0 ? 1: 0)); ;
        eggs.get(now).restore(eggs.get(i));
      }
      if (!flag) recur(now+1, cnt);

    } else {
      recur(now+1, cnt);
    }

  }
}
