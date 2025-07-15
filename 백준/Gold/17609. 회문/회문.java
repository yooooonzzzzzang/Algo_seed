
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String[] strs = new String[n];
    for (int i = 0; i < n; i++) {
      strs[i] = sc.next();
    }
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    for (int i = 0; i < n; i++) {
      int result = isPalindrome(strs[i], strs[i].length());
      if (result == -1){
        bw.write("0");
      } else{
        if (isSimilarPalindrome(strs[i], result, strs[i].length()-1-result)){
          bw.write("1");
        }else bw.write("2");
      }
      bw.newLine();
    }
    bw.flush();
    bw.close();
  }
  private static boolean isSimilarPalindrome(String ans , int a, int b) {
    if (isPalindrome(ans.substring(a+1, b+1), b+1-(a+1)) == -1 || isPalindrome(ans.substring(a,b), b-a) == -1){
      return true;
    }
    return false;
  }

  private static int isPalindrome(String ans, int len) {
    for (int i = 0; i < len / 2; i++) {
      if (ans.charAt(i) != ans.charAt(len - 1 - i)) {
        return i;
      }
    }
    return -1;
  }
}
