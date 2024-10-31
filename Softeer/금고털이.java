import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int weight = sc.nextInt();
        int types = sc.nextInt();

        HashMap<Integer, Integer> valdict = new HashMap<Integer, Integer>(types);
        for(int i=0;i<types;i++){
            int m = sc.nextInt();
            int p = sc.nextInt();

            if (valdict.containsKey(p)){
                int tmp = valdict.get(p);
                valdict.put(p, tmp+m);
            }
            else {
                valdict.put(p, m);
            }
        }

        List<Integer> keys = new ArrayList<>(valdict.keySet());
        Collections.sort(keys);
        Collections.reverse(keys);
        
        int result = 0;
        for (Integer key:keys){
            if(valdict.get(key) <= weight){
                result += key*valdict.get(key);
                weight -= valdict.get(key);
            }
            else {
                result += key*weight;
                weight = 0;
            }
        }

        System.out.println(result);
    }
}
