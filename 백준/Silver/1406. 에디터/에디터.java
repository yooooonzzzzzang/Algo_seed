
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String arr = sc.next();
    List<Character> list = new LinkedList<>();
    for (char c : arr.toCharArray()) {
      list.add(c);
    }

    int N = arr.length();
    int M = sc.nextInt();
    ListIterator<Character> it = list.listIterator(N);
    while (M-- > 0) {
      char command = sc.next().charAt(0);
      switch (command) {
          case 'L' :
          if(it.hasPrevious()){
            it.previous();
          }
          break;
          case 'D' :
          if(it.hasNext()){
            it.next();
          }
              break;
          case 'B' :
          if(it.hasPrevious()){
            it.previous();
            it.remove();
          }
              break;
          case 'P' :
          // next iterator 의 앞에 추가
            it.add(sc.next().charAt(0));
              break;
        }
      }

    StringBuilder sb = new StringBuilder();
    for (char c : list) {
      sb.append(c);
    }
    System.out.println(sb);
  }
}


