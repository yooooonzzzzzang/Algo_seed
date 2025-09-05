import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 숫자의 길이
        int K = Integer.parseInt(st.nextToken()); // 제거할 자리 수
        String num = br.readLine();               // 숫자 문자열

        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            char c = num.charAt(i);

            // 스택이 비어있지 않고, 현재 문자보다 작고, 아직 제거 횟수가 남아있으면 pop
            while (!stack.isEmpty() && K > 0 && stack.peekLast() < c) {
                stack.pollLast();
                K--;
            }
            stack.addLast(c);
        }

        // 아직 제거 횟수가 남아있으면 뒤에서 제거
        while (K > 0) {
            stack.pollLast();
            K--;
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }

        System.out.println(sb.toString());
    }
}
