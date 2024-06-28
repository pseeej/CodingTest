import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] recipe = new int[M];
        for(int i=0;i<M;i++){
            recipe[i] = sc.nextInt();
        }

        int[] inputs = new int[N];
        for(int j=0;j<N;j++){
            inputs[j] = sc.nextInt();
        }

        boolean checkIfDone = false;
        for(int i=0;i<N-M+1;i++){
            if((Arrays.toString(Arrays.copyOfRange(inputs, i, i+M))).equals(Arrays.toString(recipe))){
                checkIfDone = true;
                break;
            }
        }

        if (checkIfDone)
            System.out.println("secret");
        else
            System.out.println("normal");
    }
}
