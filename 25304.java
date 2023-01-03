import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        int N = sc.nextInt();
    
        int user = 0;
        for(int i=0;i<N;i++){
            int money = sc.nextInt();
            int amount = sc.nextInt();
            user += money * amount;
        }
    
        if (user == total)
            System.out.println("Yes");
        else
            System.out.println("No");

    }
}
