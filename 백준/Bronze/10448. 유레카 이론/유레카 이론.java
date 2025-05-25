
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class Main {

  public static void main(String[] args) {
    List<Integer> gonsik = new ArrayList<>();
    int sum = 0;
    for (int i = 1; ; i++) {
      sum = i * (i + 1) / 2;
      if (sum > 1000) break;
      gonsik.add(sum);
    }

    Set<Integer> tmpAns = new HashSet<>();
    for (int i = 0; i < gonsik.size(); i++) {
      for (int j = 0 ; j < gonsik.size(); j++) {
        for (int k = 0; k < gonsik.size(); k++) {
          tmpAns.add(gonsik.get(i) + gonsik.get(j) + gonsik.get(k));
        }
      }
    }
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    for (int i = 0; i < t; i++) {
      int target  = sc.nextInt();
      boolean didprint = false;
        if (tmpAns.contains(target)) {
          System.out.println(1);
        } else{
          System.out.println(0);
        }

    }
  }
}
