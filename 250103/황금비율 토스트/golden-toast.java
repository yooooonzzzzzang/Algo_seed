import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // n, m 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 초기 문자열 입력
        String inputString = br.readLine();
        LinkedList<Character> l = new LinkedList<>();
        for (char c : inputString.toCharArray()) {
            l.add(c);
        }

        ListIterator<Character> it = l.listIterator(l.size());
        for (int i=0; i<m; i++){
            String input =  br.readLine();

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