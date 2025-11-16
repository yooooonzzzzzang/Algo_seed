import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static char[][] arr;
    static Deque<int[]> fires;
    static Deque<int[]> q;
    static String ans;

    static void bfs() {
        int time = 0;

        while (!q.isEmpty()) {
            time++;
            
            int fireSize = fires.size();
            for (int i = 0; i < fireSize; i++) {
                int[] cur = fires.poll();
                int x = cur[0], y = cur[1];

                int[] dx = {-1, 1, 0, 0};
                int[] dy = {0, 0, -1, 1};

                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];

                    if (0 <= nx && nx < n && 0 <= ny && ny < m &&
                            (arr[nx][ny] == '.' || arr[nx][ny] == '@')) {
                        arr[nx][ny] = '*';
                        fires.add(new int[]{nx, ny});
                    }
                }
            }

            int playerSize = q.size();
            for (int i = 0; i < playerSize; i++) {
                int[] cur = q.poll();
                int x = cur[0], y = cur[1];

                int[] dx = {-1, 1, 0, 0};
                int[] dy = {0, 0, -1, 1};

                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];

                    // 맵 밖 → 탈출 성공
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                        ans = String.valueOf(time);
                        return;
                    }

                    // 이동 가능
                    if (arr[nx][ny] == '.') {
                        arr[nx][ny] = '@';
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());  // width
            n = Integer.parseInt(st.nextToken());  // height

            arr = new char[n][m];
            fires = new LinkedList<>();
            q = new LinkedList<>();

            for (int i = 0; i < n; i++) {
                String line = br.readLine();
                for (int j = 0; j < m; j++) {
                    arr[i][j] = line.charAt(j);
                    if (arr[i][j] == '*') fires.add(new int[]{i, j});
                    else if (arr[i][j] == '@') q.add(new int[]{i, j});
                }
            }

            ans = "IMPOSSIBLE";
            bfs();
            sb.append(ans).append("\n");
        }

        System.out.print(sb);
    }
}
