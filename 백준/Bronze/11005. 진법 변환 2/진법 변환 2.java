import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] inputs = br.readLine().split(" ");
    int number = Integer.parseInt(inputs[0]);
    int b = Integer.parseInt(inputs[1]);
    List<String> list = new ArrayList<>();
    while (number > 0){
      int mok = number / b;
      int na = number % b;
      if (na >= 10){
        char sna = (char)('A' + (na - 10));
        list.add(sna+"");
      } else list.add(String.valueOf(na));
      number = mok;
    }
    for (int i = list.size()-1; i >= 0; i--){
      System.out.print(list.get(i));
    }

  }
}
