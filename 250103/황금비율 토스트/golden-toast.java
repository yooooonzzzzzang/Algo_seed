import java.util.ListIterator;
import java.util.LinkedList;
import java.util.stream.Collectors;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine(); 
        // LinkedList에 바로 대입
        LinkedList<Character> l =sc.nextLine().chars()
                                       .mapToObj(c -> (char) c)
                                       .collect(Collectors.toCollection(LinkedList::new));

        ListIterator<Character> it = l.listIterator(l.size());
        for (int i=0; i<m; i++){
            String input = sc.nextLine();

            if (input.startsWith("L")){
                if(it.hasPrevious()){
                    it.previous();
                }
            } else if(input.startsWith("P")){
                char k  = input.split(" ")[1].charAt(0); 
                it.add(k);
            } else if(input.startsWith("R")){
                if(it.hasNext()){
                    it.next();
                }
            } else{
                if (it.hasNext()){
                    it.next();
                    it.remove();
                }
            }
        }

        // 출력 l 
        for(char c: l){
            System.out.print(c);
        }
    }
}