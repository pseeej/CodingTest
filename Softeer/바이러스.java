import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = sc.nextInt();
        int P = sc.nextInt();
        int N = sc.nextInt();

        long result = K;
        for(int i=0;i<N;i++){
            result *= P;
            result %= 1000000007;
        }

        System.out.println(result%1000000007);
    }
}
