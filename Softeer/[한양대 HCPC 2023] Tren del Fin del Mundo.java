import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        int resultx = 1001;
        int resulty = 1001;
        for(int i=0;i<T;i++){
            int x = sc.nextInt();
            int y = sc.nextInt();

            if (y<resulty){
                resulty = y;
                resultx = x;
            }
        }
        System.out.printf("%d %d", resultx, resulty);

        
    }
}
