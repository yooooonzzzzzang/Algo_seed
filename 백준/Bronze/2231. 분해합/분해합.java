import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int target = scanner.nextInt();
    for (int i = 1; i < target; i++) {
      int tmp  = i;
      String number = String.valueOf(i);
      for (int j = 0; j < number.length(); j++) {
        tmp += number.charAt(j) - '0';
      }
      if (tmp == target) {
        System.out.println(i);
        return;
      }
    }
    System.out.println(0);
  }
}
