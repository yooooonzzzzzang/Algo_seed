
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws IOException {
    Scanner scanner = new Scanner(System.in);
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    char[] chars = scanner.nextLine().toCharArray();
    StringBuilder sb = new StringBuilder();
    boolean inTag = false;

    for (char c : chars) {
      if (c == '<') {
        for (int j = sb.length() - 1; j >= 0; j--) bw.write(sb.charAt(j));
        sb.setLength(0);

        inTag = true;
        bw.write('<');
      } else if (c == '>') {
        inTag = false;
        bw.write('>');
      } else if (inTag) {
        bw.write(c);
      } else if (c == ' ') {
        for (int j = sb.length() - 1; j >= 0; j--) bw.write(sb.charAt(j));
        sb.setLength(0);
        bw.write(' ');
      } else {
        sb.append(c);
      }
    }

    for (int j = sb.length() - 1; j >= 0; j--) bw.write(sb.charAt(j));

    bw.flush();
  }
}
