import java.io.*;
import java.util.*;

public class Main {

    public static int countnum(boolean[] num){
        int result = 0;
        for(int i=0;i<7;i++){
            if(num[i])
                result += 1;
        }

        return result;
    }

    public static int numdiff(boolean[] num1, boolean[] num2){
        int result = 0;
        for(int i=0;i<num1.length;i++){
            if (num1[i] != num2[i])
                result += 1;
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        ArrayList<boolean[]> currbolds = new ArrayList<>();

        boolean[] zero = {true, true, true, false, true, true, true};
        currbolds.add(zero);
        boolean[] one = {false, false, true, false, false, true, false};
        currbolds.add(one);
        boolean[] two = {true, false, true, true, true, false, true};
        currbolds.add(two);
        boolean[] three = {true, false, true, true, false, true, true};
        currbolds.add(three);
        boolean[] four = {false, true, true, true, false, true, false};
        currbolds.add(four);
        boolean[] five = {true, true, false, true, false, true, true};
        currbolds.add(five);
        boolean[] six = {true, true, false, true, true, true, true};
        currbolds.add(six);
        boolean[] seven = {true, true, true, false, false, true, false};
        currbolds.add(seven);
        boolean[] eight = {true, true, true, true, true, true, true};
        currbolds.add(eight);
        boolean[] nine = {true, true, true, true, false, true, true};
        currbolds.add(nine);

        for(int i=0;i<T;i++){
            int bef = sc.nextInt();
            int aft = sc.nextInt();

            String sbef = String.valueOf(bef);
            //System.out.println(sbef);
            String saft = String.valueOf(aft);
            //System.out.println(saft);

            String finbef = "";
            String finaft = "";

            for(int j=0;j<5-sbef.length();j++){
                finbef += " ";
            }
            finbef += sbef;

            for(int j=0;j<5-saft.length();j++){
                finaft += " ";
            }
            finaft += saft;

            int result = 0;

            //System.out.printf("%d %d%n", finbef.length(), finaft.length());

            for(int j=0;j<5;j++){
                if(finbef.charAt(j) == ' ' && finaft.charAt(j) != ' ')
                    //System.out.println(currbolds.size());
                    //System.out.println(currbolds.get(Integer.valueOf(finaft.charAt(j))-'0'));
                    result += countnum(currbolds.get(Integer.valueOf(finaft.charAt(j))-'0'));
                    
                else if(finbef.charAt(j) != ' ' && finaft.charAt(j) == ' ')
                    result += countnum(currbolds.get(Integer.valueOf(finbef.charAt(j))-'0'));
                
                else if(finbef.charAt(j) != finaft.charAt(j)){
                    result += numdiff(currbolds.get(Integer.valueOf(finbef.charAt(j))-'0'), currbolds.get(Integer.valueOf(finaft.charAt(j))-'0'));
                }
            }

            System.out.println(result);
        }
    }
}
