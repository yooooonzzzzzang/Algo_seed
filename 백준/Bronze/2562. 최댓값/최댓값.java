import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
    int[] arr =new int[9];
    Scanner sc = new Scanner(System.in);
    for (int i=0; i<arr.length; i++){
        int k = sc.nextInt();
        arr[i] = k;
    }
    int maxnum = 0;
    int maxindex =0;
    for(int i=0; i<arr.length; i++){
        if (maxnum < arr[i]){
            maxnum = arr[i];
            maxindex = i;
        }
    }
    System.out.println(maxnum);
    System.out.println(maxindex + 1);
    }
    
}
