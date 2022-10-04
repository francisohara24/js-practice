import java.util.Scanner;

public class _18_java_anagrams {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String a = input.next();
        String b = input.next();

        System.out.println(isAnagram(a,b)?"Anagrams":"Not Anagrams");
    }

    public static boolean isAnagram(String a, String b){
        int count = 0;
        String temp = b;
        for(int i = 0; i < a.length(); i ++){
            for(int j = 0; j < temp.length(); j++){
                if(a.substring(i,i+1).equalsIgnoreCase(temp.substring(j, j+1))){
                    count ++;
                    temp = temp.substring(0,j) + temp.substring(j+1);
                    break;
                }
            }
        }
        return a.length()==b.length() && count==a.length();
    }


}