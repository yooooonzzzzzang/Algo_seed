import java.util.Stack;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        Stack<Integer>s = new Stack<>();
        int n = sc.nextInt();
        for (int i=0; i<n; i++){
            String commands = sc.next();
            if(commands.equals("push")){
                int x = sc.nextInt();
                s.push(x);
            } 
            else if(commands.equals("pop")){
                System.out.println(s.pop());
            }
            else if(commands.equals("size")){
                System.out.println(s.size());
            } else if(commands.equals("empty")){
                if(s.isEmpty()){
                    System.out.println(1);
                } else{
                    System.out.println(0);
                }
            } else{
                System.out.println(s.peek());
            }
            
        }
        // s.push
    }
}