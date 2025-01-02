import java.util.Scanner;

public class Main {
    public static final int MAX_N = 100;
    
    public static int n;
    public static int[] arr = new int[MAX_N];

    public static void bubbleSort() {
        boolean sorted = true;

        do {
            sorted = true;
            for(int i = 0; i < n - 1; i++)
                if(arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    sorted = false;
                }
        } while(!sorted);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 입력
        n = sc.nextInt();
        for(int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        bubbleSort();

        for(int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }
}