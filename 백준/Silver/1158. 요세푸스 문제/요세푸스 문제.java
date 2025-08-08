
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.Scanner;
import java.util.stream.IntStream;


/*
* 방법1.
* removed 배열과 ( curIdx + 1 ) % N 을 이용
* nklogn
*
* 방법2
* 실제로 삭제 arr[j-1] = arr[j];
* n2
*
* 방법3
* 방법2를 list 를 이용
* */
public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int K = sc.nextInt();
    int[] ans = new int[N];
    List<Integer> array = new ArrayList<>(N);
    for (int i = 1; i <= N; i++) {
      array.add(i);
    }

    int curIndex = 0;
    for (int i = 0; i < N; i++) {
      // remove 시 삭제되기 때문에 한칸 앞으로 구하기 위해 -1
      curIndex = (curIndex + K -1) % array.size();
      ans[i] = array.remove(curIndex);
    }
    System.out.print("<");
    for (int i = 0; i < N; i++) {
      if (i > 0) {
        System.out.print(", ");
      }
      System.out.print(ans[i]);
    }
    System.out.print(">");
  }
}
