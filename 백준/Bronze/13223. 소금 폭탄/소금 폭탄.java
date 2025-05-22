import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String start = br.readLine();
    String end = br.readLine();

    String[] splitStart = start.split(":");
    String[] splitEnd = end.split(":");
    int totalEnd = Integer.parseInt(splitEnd[0]) * 60 * 60 + Integer.parseInt(splitEnd[1]) * 60 + Integer.parseInt(splitEnd[2]);
    int totalStart = Integer.parseInt(splitStart[0]) * 60 * 60 + Integer.parseInt(splitStart[1]) * 60 + Integer.parseInt(splitStart[2]);
    int diff = totalEnd - totalStart;
    if (diff <= 0) {
      diff += 24 * 60 * 60;
    }

    int hour = diff / ( 60 * 60);
    int minute = diff % 3600 / 60;
    int second = diff % 60;
    String result = String.format("%02d:%02d:%02d", hour, minute, second);
    System.out.println(result);

  }

}
