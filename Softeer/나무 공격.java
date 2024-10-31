import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int row = sc.nextInt();
        int col = sc.nextInt();

        int[][] board = new int[row][col];
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                board[i][j] = sc.nextInt();
            }
        }

        int start1 = sc.nextInt();
        int end1 = sc.nextInt();
        int start2 = sc.nextInt();
        int end2 = sc.nextInt();

        int[] rowcnt = new int[row];
        for(int i=0;i<row;i++){
            rowcnt[i] = 0;
        }

        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(board[i][j] == 1)
                    rowcnt[i] += 1;
            }
        }

        for(int i=start1-1;i<=end1-1;i++){
            if(rowcnt[i] > 0)
                rowcnt[i] -= 1;
        }

        for(int i=start2-1;i<=end2-1;i++){
            if(rowcnt[i] > 0)
                rowcnt[i] -= 1;
        }


        int result = 0;
        for(int i=0;i<row;i++)
            result += rowcnt[i];

        System.out.print(result);
    }
}
