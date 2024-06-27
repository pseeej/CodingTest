import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int i=0;i<T;i++){
            int votes = sc.nextInt();
            String result = "";
            
            for (int j=0;j<Integer.valueOf(votes/5);j++){
                result += "++++ ";
            }
            
            for (int j=0; j<Integer.valueOf(votes%5); j++){
                result = result + "|";
            }
            
            System.out.println(result);
            
        }
    }
}
