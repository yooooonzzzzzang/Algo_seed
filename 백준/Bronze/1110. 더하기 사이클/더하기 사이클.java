import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int j = 0;
        int cnt = 0;
        int newnum = 0;
        int k = 0;
        int origin_n=n;
        do{
            if (n<10){
                j = 0;
            }else{
                j= n/10;
                n = n % 10;
            }
            k = j + n;

            n = Integer.parseInt(Integer.toString(n)+ Integer.toString(k%10));
        
            cnt ++;
        }while(n!=origin_n);
        System.out.println(cnt);
    }
}
