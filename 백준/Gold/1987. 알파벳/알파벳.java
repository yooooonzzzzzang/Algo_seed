
import java.util.Scanner;

public class Main {
    static int r, c;
    static char[][] arr;
    static int ans;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        r = sc.nextInt();
        c = sc.nextInt();
        arr = new char[r][c];

        for (int i = 0; i < r; i++) {
            String s = sc.next();
            for (int j = 0; j < c; j++) {
                arr[i][j] = s.charAt(j);
            }
        }

        int startMask = 1 << (arr[0][0] - 'A'); // 시작 알파벳 사용 표시
        recur(0, 0, 1, startMask);
        System.out.println(ans);
    }

    public static void recur(int x, int y, int cnt, int mask) {
        ans = Math.max(ans, cnt);

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx < 0 || ny < 0 || nx >= r || ny >= c) continue;

            int next = arr[nx][ny] - 'A';

            // 이미 방문한 알파벳이면 스킵
            if ((mask & (1 << next)) != 0) continue;

            // 새로운 상태로 탐색
            recur(nx, ny, cnt + 1, mask | (1 << next));
        }
    }
}
