import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int result = 0;
        for(int i=0;i<5;i++){
            String start = sc.next();
            String end = sc.next();

            String[] starts = start.split(":");
            String[] ends = end.split(":");

            int workedmin = Integer.valueOf(ends[1])-Integer.valueOf(starts[1]);
            int workedhr = (Integer.valueOf(ends[0])-Integer.valueOf(starts[0]))*60;
            result += workedhr+workedmin;
        }

        System.out.println(result);
    }
}
