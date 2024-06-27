import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        ArrayList<Integer> houses = new ArrayList<>();

        for(int i=0;i<n;i++){
            houses.add(sc.nextInt());
        }

        int mindist = 1000001;
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if(houses.get(j)-houses.get(i) < mindist)
                    mindist = houses.get(j)-houses.get(i);
            }
        }

        //System.out.println(mindist);

        int result = 0;
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if(houses.get(j)-houses.get(i) == mindist)
                    result += 1;
            }
        }

        System.out.println(result);
    }
}
