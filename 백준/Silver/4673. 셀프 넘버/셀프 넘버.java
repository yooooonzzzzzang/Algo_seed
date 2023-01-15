import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static int selfnum(int n){
        int dn = n;
        while(n>0){
            dn += n % 10;
            n/=10;
        }
        return dn;

    }
    public static void main(String[] args) throws Exception {
        int [] arr = IntStream.rangeClosed(0, 10000).toArray();
        for (int i=1; i<=10000; i++){
            
            int index = selfnum(i);
            if (index <= 10000)
                arr[index] = 0;
        }
        for (int i=1; i<=10000; i++){
            if (arr[i] != 0){
                System.out.println(arr[i]);
            }
        }
       
    }
}