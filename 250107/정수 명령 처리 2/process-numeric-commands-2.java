import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Queue<Integer> q = new LinkedList<>();
        for (int i=0; i<n; i++){
            String command = sc.next();
            if (command.equals("push")){
                int x = sc.nextInt();
                q.add(x);

            } else if (command.equals("pop")){
                System.out.println(q.poll());

            } else if (command.equals("size")){
                System.out.println(q.size());

            } else if (command.equals("empty")){
                if (q.isEmpty()){
                    System.out.println(1);
                } else{
                    System.out.println(0);
                }

            } else {
                System.out.println(q.peek());
            }
        }

    }
}