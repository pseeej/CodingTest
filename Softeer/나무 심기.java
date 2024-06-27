import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        ArrayList<Integer> nums = new ArrayList<>();
        for(int i=0;i<n;i++){
            nums.add(sc.nextInt());
        }

        int result = -101;
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if(nums.get(i)*nums.get(j) > result)
                    result = nums.get(i)*nums.get(j);
            }
        }

        System.out.println(result);
    }
}
