
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static char[] arr;
  static int[] cntArr;
  static int[] pwArr;

  static int convert(char chr){
    if(chr == 'A'){
      return 0;
    } else if (chr == 'C') {
      return 1;
    } else if (chr =='G') {
      return 2;
    } else if (chr == 'T') {
      return 3;
    } else return -1;
  }


  static boolean isValid(int[] cntArr, int[] pwArr) {
    for (int i = 0; i < pwArr.length; i++) {
      if (cntArr[i] < pwArr[i]) {
        return false;
      }
    }
    return true;
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int s = sc.nextInt();
    int p = sc.nextInt();
    arr = sc.next().toCharArray();
    pwArr = new int[4];
    for (int i = 0; i < 4; i++) {
      pwArr[i] = sc.nextInt();
    }
    cntArr = new int[4];
    int ans = 0;
    // 1. 투포인턴 처음 전처리 > p 보다 1작게 이따 추가
    for (int i = 0; i < p-1; i++) {
      cntArr[convert(arr[i])]++;
    }
    // 2, 투포인터로 옮기기 + count 확인하고 + 맨 앞 빼주기
    for (int i = p-1; i < s; i++) {
      cntArr[convert(arr[i])]++;
      if(isValid(cntArr, pwArr)){
        ans++;
      }
      cntArr[convert(arr[i-p+1])]--;
    }

    System.out.println(ans);
  }

}
