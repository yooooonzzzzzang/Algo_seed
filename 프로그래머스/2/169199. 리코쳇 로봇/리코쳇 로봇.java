import java.util.*;
class Solution {
    public int solution(String[] board) {
        int n = board.length;
        int m = board[0].length();
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        int sx = 0, sy = 0;
        
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                if (board[i].charAt(j) =='R'){
                    sx = i; sy = j;
                }
            }
        }
        int[][] visited = new int[n][m];
        for (int[] row: visited) Arrays.fill(row, -1);
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{sx, sy});
        visited[sx][sy] = 0;
        
        while(!queue.isEmpty()){
            int[] cur = queue.poll();
            int cx = cur[0], cy = cur[1];
            
            for(int d=0; d<4; d++){
                int nx = cx, ny = cy;
                
                while (true){
                    int nnx = nx + dx[d];
                    int nny = ny + dy[d];
                     // 범위 밖이거나 D면 멈춤
                    if (nnx < 0 || nnx >= n || nny < 0 || nny >= m || board[nnx].charAt(nny) == 'D') {
                        break;
                    }
                    
                    nx = nnx;
                    ny = nny;
                    
                    
                }
        
            // 멈춘 칸이 G면 정답
            if (board[nx].charAt(ny) == 'G') {
                return visited[cx][cy] + 1;
            }
            
          // 미방문 칸이면 큐에 추가
            if (visited[nx][ny] == -1) {
                visited[nx][ny] = visited[cx][cy] + 1;
                queue.add(new int[]{nx, ny});
            }
            }
        }
        return -1;
        
    }
}