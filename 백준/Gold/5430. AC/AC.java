import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int T = Integer.parseInt(br.readLine());

    while (T-- > 0) {
      String p = br.readLine().trim();         // 명령어
      int N = Integer.parseInt(br.readLine()); // 원소 개수(참고용)
      String input = br.readLine().trim();     // 예: [1,2,3] 또는 []

      // 입력 파싱: []도 정상 처리
      Deque<Integer> arr = new ArrayDeque<>();
      if (input.length() >= 2) {
        String body = input.substring(1, input.length() - 1).trim(); // 대괄호 제거
        if (!body.isEmpty()) {
          for (String s : body.split(",")) {
            arr.add(Integer.parseInt(s.trim()));
          }
        }
      }

      boolean isReversed = false;
      boolean isValid = true;

      for (int i = 0; i < p.length(); i++) {
        char c = p.charAt(i);
        if (c == 'R') {
          isReversed = !isReversed;
        } else if (c == 'D') {
          if (arr.isEmpty()) {
            isValid = false;
            break;
          }
          if (!isReversed) arr.pollFirst();
          else arr.pollLast();
        }
      }

      if (!isValid) {
        bw.write("error\n");
        continue; // 다음 테스트케이스로
      }

      // 출력
      StringBuilder sb = new StringBuilder("[");
      Iterator<Integer> it = isReversed ? arr.descendingIterator() : arr.iterator();
      while (it.hasNext()) {
        sb.append(it.next());
        if (it.hasNext()) sb.append(",");
      }
      sb.append("]");
      bw.write(sb.toString());
      bw.newLine();
    }
    bw.flush();
  }
}
