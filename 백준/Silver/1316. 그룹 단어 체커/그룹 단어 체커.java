import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.StringTokenizer;

// n = int(input())
// cnt = 0
// for _ in range(n):
//     words = input()
//     wordlen = len(words)
//     arr = []

//     for i in range(wordlen):
//         if words[i] not in arr:
//             arr.append(words[i])
//         else:
//             # 안되는 애들
//             if words[i-1] != words[i]:
//                 cnt += 1
//                 break

// print(n-cnt)

public class Main {
    public static void main(String[] args) throws IOException {

        	
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N=Integer.parseInt(br.readLine());
    int cnt=0;
    for(int i=0; i<N; i++){
        String word=br.readLine();
        List<Character> list=new ArrayList<>();
        for(int j=0; j<word.length(); j++){
            if(!list.contains(word.charAt(j))){
                list.add(word.charAt(j));
            }else{
                if(word.charAt(j-1)!=word.charAt(j)){
                    cnt++;
                    break; 
                }
            }
        }
    }
    System.out.println(N-cnt);
}
}