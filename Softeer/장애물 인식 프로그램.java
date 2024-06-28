import java.io.*;
import java.util.*;

public class Main {

    static int[][] visited = new int[26][26];

    public static int DFS(int[][] pan, int y, int x, int cnt, int size){
        int result = cnt;
        //System.out.printf("%d %d %d %n", y, x, result);

        int[] dy = {0, 1, 0, -1};
        int[] dx = {1, 0, -1, 0};

        for(int i=0;i<4;i++){
            if (y+dy[i] >= 0 && x+dx[i] >= 0 && y+dy[i] < size && x+dx[i] < size && pan[y+dy[i]][x+dx[i]] == 1 && visited[y+dy[i]][x+dx[i]] != 1){
                visited[y+dy[i]][x+dx[i]] = 1;
                result = DFS(pan, y+dy[i], x+dx[i], result+1, size);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[][] board = new int[N][N];
        String tmp = "";
        for(int i=0;i<N;i++){
            tmp = sc.next();
            for(int j=0;j<N;j++){
                board[i][j] = Integer.valueOf(tmp.charAt(j))-'0';
            }
        }

        ArrayList<Integer> results = new ArrayList<>();
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                visited[i][j] = 0;
        
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(board[i][j]==1 && visited[i][j] != 1){
                    visited[i][j] = 1;
                    results.add(DFS(board, i, j, 1, N));
                }
            }
        }

        Collections.sort(results);
        System.out.println(results.size());
        for(int i=0;i<results.size();i++){
            System.out.println(results.get(i));
        }
    }

}
