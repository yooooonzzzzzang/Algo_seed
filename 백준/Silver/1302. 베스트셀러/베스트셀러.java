
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;
import java.util.stream.Stream;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    Map<String, Integer> map = new TreeMap<>();
    for (int i = 0; i < N; i++) {
      String title = br.readLine();
      map.put(title, map.getOrDefault(title, 0) + 1);
    }
    String maxTitle = "";
    int maxCount = 0;
    for (Entry<String, Integer> m : map.entrySet()) {
      if (m.getValue() > maxCount){
        maxCount = m.getValue();
        maxTitle = m.getKey();
      }
    }
    System.out.println(maxTitle);
  }
}
