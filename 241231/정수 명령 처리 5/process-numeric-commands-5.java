import java.util.*;
public class Main {
    static ArrayList<Integer> arr = new ArrayList<>();

    static void push_back(int num){
        arr.add(num);
    }
    static void pop_back(){
        if(!arr.isEmpty()){
            arr.remove(arr.size()-1);
        }
    }
    static void size(){
        System.out.println(arr.size());
    }
    static void get(int num){
        System.out.println(arr.get(num-1));
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i=0; i<n; i++){
            String methods = sc.next();
            if (methods.equals("push_back")){
                int nums = sc.nextInt();
                push_back(nums);

            }else if(methods.equals("pop_back")){
                pop_back();

            }else if(methods.equals("size")){
                size();

            }else{ // get
                int nums = sc.nextInt();
                get(nums);
            }
         
        }
    }
}