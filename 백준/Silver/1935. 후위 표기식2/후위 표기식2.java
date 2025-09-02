
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    char[] arr = sc.next().toCharArray();
    double[] nums = new double[N];
    for (int i = 0; i < N; i++) {
      nums[i] = sc.nextDouble();
    }

    Deque<Double> stack = new ArrayDeque<>();
    for (char c : arr) {
      if ('A' <= c && c < 'A'+ N ){
        stack.push(nums[c-'A']);
      } else {
        Double b = stack.pop();
        Double a = stack.pop();

        switch (c){
          case '+': stack.push(a+b); break;
          case '-': stack.push(a-b); break;
          case '*': stack.push(a*b); break;
          case '/': stack.push(a/b); break;
          default:
            throw new IllegalArgumentException("Invalid input");
        }

      }
    }

    System.out.printf("%.2f",stack.pop());



    }

  }
