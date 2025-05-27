import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int k = scanner.nextInt();
    char [] arr = new char[n];
    Arrays.fill(arr, '?');
    int index = 0;
    boolean flag = false;
    while (k -- > 0) {
      int cnt = scanner.nextInt();
      char letter = scanner.next().charAt(0);
      // + n ) % n 음수 방지
      index = ((index - cnt) % n + n )% n;
      if (arr[index] != '?' && arr[index] != letter) {
        System.out.println("!");
        return;
      } else {
        arr[index] = letter;
      }

    }
    boolean [] used = new boolean[26];
    for (int i = 0; i < n; i++) {
      if(arr[i] == '?'){continue;}
      if(used[arr[i] - 'A']) {
        System.out.println("!");
        return;
      }
      used[arr[i] - 'A'] = true;
    }
    
    for (int i = 0; i < n; i++) {
      System.out.print(arr[(index+i)%n] );
    }
  }
}
