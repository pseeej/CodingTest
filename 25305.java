import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int k = sc.nextInt();

        int[] scores = new int[N];

        for(int i=0;i<N;i++){
            scores[i] = sc.nextInt();
        }

        Arrays.sort(scores);

        System.out.println(scores[N-k]);
        
    }
}
