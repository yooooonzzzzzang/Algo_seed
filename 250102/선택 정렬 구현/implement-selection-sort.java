import java.util.Scanner;
public class Main {
    static int n;
    static int [] arr;
    static int MAX_NUM = 101;
    static void selection_Sort(){
        for (int i=0; i<n-1; i++){
            int min_n = i;
            for (int j = i+1; j<n; j++){
                if (arr[min_n] > arr[j]){
                    min_n = j;
                }
            }
            int tmp = arr[i];
            arr[i] = arr[min_n];
            arr[min_n] = tmp;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n];
        for (int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }

        selection_Sort();
        for (int i=0; i<n; i++){
            System.out.print(arr[i] + " ");
        }
    }
}