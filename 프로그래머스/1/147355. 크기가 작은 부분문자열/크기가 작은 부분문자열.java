class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int n = p.length();
        System.out.println(n);
        
        for (int i=0; i<t.length()-n+1; i++){
            String tmp ="";
            for (int j=0; j<n ; j++){
                tmp += t.charAt(j+i);
            }
             if (Long.parseLong(tmp) <= Long.parseLong(p)) answer ++;
            
        }
        return answer;
    }
}