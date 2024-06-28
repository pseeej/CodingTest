import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = new int[8];
        for(int i=0;i<8;i++){
            nums[i] = sc.nextInt();
        }

        boolean checkIfDone = true;
        for(int i=0;i<8;i++){
            if (nums[i]!=i+1){
                checkIfDone = false;
                break;
            }
        }
        if(checkIfDone){
            System.out.println("ascending");
            return;
        }

        checkIfDone = true;
        for(int i=0;i<8;i++){
            if(nums[i]!=8-i){
                checkIfDone = false;
                break;
            }
        }
        if (checkIfDone){
            System.out.println("descending");
            return;
        }

        System.out.println("mixed");
    }
}
