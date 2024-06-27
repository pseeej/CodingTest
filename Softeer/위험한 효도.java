import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int d = sc.nextInt();

        int curr = 0;
        int time = 0;
        boolean turn = true; // 술래 기준
        boolean touched = false;
        while (curr < 2*d){
            if (turn){
                if (!touched && curr+a >= d){
                    time += (d-curr);
                    curr = d;
                    
                    touched = !touched;
                    int tmp = a;
                    a = b;
                    b = tmp; 
                    
                    turn = !turn;
                }
                else{
                    curr += a;
                    time += a;
                }
            }
            else
                time += b;

            //System.out.printf("%b %d %d\n", turn, curr, time);
            turn = !turn;
        }

        System.out.println(time-(curr-2*d));
    }
}
