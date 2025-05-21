
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    int ans = 0;
    String text = bufferedReader.readLine();
    String search = bufferedReader.readLine();

    int idx = 0;
    while ((idx = text.indexOf(search, idx)) != -1) {
      ans ++;
      idx += search.length();
    }
    System.out.println(ans);

  }
}
