import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < enemy.length; i++) {
            maxHeap.offer(enemy[i]);
            n -= enemy[i];

            if (n < 0) {
                if (k > 0) {
                    // 가장 큰 enemy에 무적권 사용
                    n += maxHeap.poll();
                    k--;
                } else {
                    return i; // 현재 라운드 진입 불가
                }
            }
        }

        return enemy.length; // 전부 클리어
    }
}