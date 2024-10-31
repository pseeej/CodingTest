import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] houses = new int[N];
        for(int i=0;i<N;i++){
            houses[i] = sc.nextInt();
        }

        Arrays.sort(houses);

        int result = 0;
        for(int r=2;r<=houses[N-1];r++){
            int tmpcnt = 0;
            for(int i=0;i<N;i++){
                if(houses[i]%r==0){
                    tmpcnt += 1;
                }
            }
            if (result < tmpcnt)
                result = tmpcnt;
        }

        System.out.println(result);
    }
}
