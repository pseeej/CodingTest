import java.io.*;
import java.util.*;

public class Main {
    public static int getIdx(String name, String[] arr){
        for (int i=0;i<arr.length;i++){
            if(arr[i].equals(name))
                return i;
        }

        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nameN = sc.nextInt();
        int timeN = sc.nextInt();

        String[] names = new String[nameN];
        for(int i=0;i<nameN;i++){
            String name = sc.next();
            names[i] = name;
        }
        Arrays.sort(names);

        boolean[][] rooms = new boolean[nameN][];
        boolean[] times = new boolean[19];
        for(int i=0;i<19;i++)
            times[i] = true;

        for(int i=0;i<nameN;i++){
            rooms[i] = times.clone();
        }
        
        for(int i=0;i<timeN;i++){
            String roomname = sc.next();
            int starttime = sc.nextInt();
            int endtime = sc.nextInt();

            int roomidx = getIdx(roomname, names);
            for(int j=starttime;j<endtime;j++){
                rooms[roomidx][j] = false;
            }

            //System.out.println(names[roomidx]);
            //System.out.println(Arrays.toString(Arrays.copyOfRange(rooms[getIdx(names[roomidx], names)], 9, 19)));
        }

        for(int i=0;i<nameN;i++){
            
        }

        for(int i=0;i<nameN;i++){
            System.out.printf("Room %s:%n", names[i]);
            ArrayList<Integer> availables = new ArrayList<>();
            int starttime = 0;
            int endtime = 0;
            for(int j=9;j<18;j++){
                if(rooms[i][j] && (j-1<9 || (j-1>=9 && !rooms[i][j-1])))
                    starttime = j;
                else if (!rooms[i][j] && endtime < starttime){
                    endtime = j;
                    availables.add(starttime);
                    availables.add(endtime);
                }
            }
            if(starttime>endtime){
                endtime = 18;
                availables.add(starttime);
                availables.add(endtime);
            }
            
            if(starttime==endtime)
                System.out.println("Not available");
            else{
                System.out.printf("%d available:%n", availables.size()/2);
                for(int j=0;j<availables.size();j+=2){
                    System.out.printf("%02d-%02d%n", availables.get(j), availables.get(j+1));
                }
            }
            if(i<nameN-1)
                System.out.println("-----");
        }
    }
}
