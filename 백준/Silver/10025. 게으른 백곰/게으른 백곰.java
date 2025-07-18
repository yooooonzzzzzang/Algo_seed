import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // 얼음 양동이 수
        int K = sc.nextInt(); // 한쪽으로 닿을 수 있는 거리

        int[] arr = new int[1_000_001]; // 얼음 위치 배열
        int maxPos = 0;

        // 얼음 양동이 정보 입력
        for (int i = 0; i < N; i++) {
            int g = sc.nextInt(); // 얼음 양
            int x = sc.nextInt(); // 위치
            arr[x] = g;
            maxPos = Math.max(maxPos, x);
        }

        int windowSize = 2 * K + 1;
        long currSum = 0;
        long maxSum = 0;

        // 초기 윈도우 구간 합 (0 ~ windowSize - 1까지)
        for (int i = 0; i < windowSize && i <= maxPos; i++) {
            currSum += arr[i];
        }
        maxSum = currSum;

        // 슬라이딩 윈도우 이동 (왼쪽에서 오른쪽으로)
        for (int i = windowSize; i <= maxPos; i++) {
            currSum = currSum - arr[i - windowSize] + arr[i];
            maxSum = Math.max(maxSum, currSum);
        }

        System.out.println(maxSum);
    }
}
