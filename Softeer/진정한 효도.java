import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] board = new int[3][3];
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                board[i][j] = sc.nextInt();
            }
        }


        int cost = 999;
        for(int i=0;i<3;i++){
            // 가로
            int lowest = 999;
            int highest = 0;
            // System.out.println(lowest);
            for(int j=0;j<3;j++){
                lowest = Math.min(lowest, board[i][j]);
                highest = Math.max(highest, board[i][j]);
            }

            int l_tmpcost = 0;
            int h_tmpcost = 0;
            for(int j=0;j<3;j++){
                l_tmpcost += board[i][j] - lowest;
                h_tmpcost += highest - board[i][j];
                
            }
            cost = Math.min(cost, l_tmpcost);
            cost = Math.min(cost, h_tmpcost);

            // 세로
            lowest = 999;
            highest = 0;
            for(int j=0;j<3;j++){
                lowest = Math.min(lowest, board[j][i]);
                highest = Math.max(highest, board[j][i]);
            }

            l_tmpcost = 0;
            h_tmpcost = 0;
            for(int j=0;j<3;j++){
                l_tmpcost += board[j][i] - lowest;
                h_tmpcost += highest - board[j][i];
                
            }
            cost = Math.min(cost, l_tmpcost);
            cost = Math.min(cost, h_tmpcost);
        }

        System.out.println(cost);

    }
}
