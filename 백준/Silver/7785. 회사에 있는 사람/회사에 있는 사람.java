
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    ArrayList<String[]> list = new ArrayList<>();
    for (int i = 1; i <= N; i++) {
      String[] input = br.readLine().split(" ");
      list.add(input);
    }
    list.sort(Comparator.comparing(a -> a[0]));
    ArrayList<String> res = new ArrayList();
    int cnt = 1;
    String name = list.get(0)[0];
    for (int i = 1; i < list.size(); i++) {
      if (list.get(i)[0].equals(name)) {
        cnt += 1;
      } else {
        if (cnt % 2 == 1) {
          res.add(list.get(i - 1)[0]);
        }
        cnt = 1;
        name = list.get(i)[0];
      }
    }
    if (cnt % 2 == 1) {
      res.add(list.get(list.size()-1)[0]);
    }
    res.sort(Comparator.reverseOrder());
    for (String r : res) {
      System.out.println(r);
    }
  }
}
