
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

class User {
  int age;
  String name;

  public User(int age, String name) {
    this.age = age;
    this.name = name;
  }
}
public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    User[] users = new User[N];
    for (int i = 0; i < N; i++) {
      String[] input = br.readLine().split(" ");
      users[i] = new User(Integer.parseInt(input[0]), input[1]);
    }
    Arrays.sort(users, Comparator.comparingInt(u -> u.age));
    for (int i = 0; i < N; i++) {
      System.out.println(users[i].age + " " + users[i].name);
    }
  }
}
