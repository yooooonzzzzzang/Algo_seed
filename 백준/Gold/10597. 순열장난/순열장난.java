
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
  // 1~50
  static boolean[] visited;
  static char[] arr;
  static int N;
  static ArrayList<Integer> list;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    arr = sc.nextLine().toCharArray();
    N = findN(arr);
    visited = new boolean[N + 1];   // 1~N까지 사용
    list = new ArrayList<>();
    recur(0, 1);
    recur(0, 2);
  }

  private static int findN(char[] arr) {
    int len = arr.length;
    if (len < 10) return len;
    return 9 + (len - 9) / 2;
  }

  static void recur(int idx, int jari) {
    if (idx == arr.length) {
      // 끝까지 성공적으로 분해한 경우
      for (int num : list) {
        System.out.print(num + " ");
      }
      System.out.println();
      System.exit(0);
      return;
    }

    if (jari == 1) {
      int num = arr[idx] - '0';   // char → int
      if (num >= 1 && num <= N && !visited[num]) {
        visited[num] = true;
        list.add(num);
        recur(idx + 1, 1);
        recur(idx + 1, 2);
        visited[num] = false;
        list.remove(list.size() - 1);
      }
    } else { // jari == 2
      if (idx + 1 < arr.length) { // 범위 체크
        int num = Integer.parseInt("" + arr[idx] + arr[idx + 1]);
        if (num >= 1 && num <= N && !visited[num]) {
          visited[num] = true;
          list.add(num);
          recur(idx + 2, 1);
          recur(idx + 2, 2);
          visited[num] = false;
          list.remove(list.size() - 1);
        }
      }
    }
  }
}
