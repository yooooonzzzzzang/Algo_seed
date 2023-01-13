import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int ans_h = 0;
        int ans_m = 0;
        if (N == 0 && M < 45){
            N = 24;
        }
        int total_m =  N * 60 + M - 45;
        ans_h = total_m / 60;
        ans_m = total_m % 60;
        System.out.println(ans_h +" "+ ans_m);

    }
}
