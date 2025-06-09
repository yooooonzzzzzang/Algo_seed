
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  static class Meeting implements Comparable<Meeting> {
    int start;
    int end;

    public Meeting(int start, int end) {
      this.start = start;
      this.end = end;
    }

    @Override
    public int compareTo(Meeting o) {
      if (this.end == o.end) {
        return this.start - o.start;
      }
      return this.end - o.end;
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    Meeting[] meetings = new Meeting[N];
    for (int i = 0; i < N; i++) {
      meetings[i] = new Meeting(sc.nextInt(), sc.nextInt());
    }
    Arrays.sort(meetings);
    int ans = 1;
    int curEnd = meetings[0].end;
    for (int i = 1; i < meetings.length; i++) {
      if (curEnd <= meetings[i].start) {
        ans ++;
        curEnd = meetings[i].end;
      }
    }
    System.out.println(ans);
  }
}
