import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
  public static class Message{
    int num;
    int index;

    public Message(int num, int index) {
      this.num = num;
      this.index = index;
    }
  }
  public static class Frequency{
    public int num;
    public int cnt;
    public int firstIndex;

    public Frequency(int num, int cnt, int firstIndex) {
      this.num = num;
      this.cnt = cnt;
      this.firstIndex = firstIndex;
    }
  }

  public static void main(String[] args) throws IOException {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int C = sc.nextInt();
    Message[] message = new Message[N];
    for (int i = 0; i < N; i++) {
      message[i] = new Message(sc.nextInt(), i);
    }
    Arrays.sort(message, new Comparator<Message>() {
      @Override
      public int compare(Message o1, Message o2) {
        return o1.num-o2.num;
      }
    });

    Frequency[] freq = new Frequency[N];
    int frequencyIndex = 0;
    freq[frequencyIndex] = new Frequency(message[0].num, 1, message[0].index);
    for (int i = 1; i < N; i++) {
      if (message[i].num != message[i - 1].num) {
        freq[++frequencyIndex] = new Frequency(message[i].num, 0, message[i].index);
      }
      freq[frequencyIndex].cnt++;
    }

    Arrays.sort(freq, 0, frequencyIndex + 1, new Comparator<Frequency>() {
      @Override
      public int compare(Frequency o1, Frequency o2) {
        if (o1.cnt == o2.cnt) {
          return o1.firstIndex - o2.firstIndex;
        }
        return o2.cnt - o1.cnt;
      }
    });

    for (int i = 0; i <= frequencyIndex; i++) {
      while(freq[i].cnt-- > 0){
        System.out.print(freq[i].num + " ");
    }
  }
    System.out.println();
}}
