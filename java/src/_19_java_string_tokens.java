import java.util.Scanner;
import java.util.ArrayList;

public class _19_java_string_tokens {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String s = input.nextLine() + " ";
        int n;
        String temp = "";
        ArrayList<String> result = new ArrayList<>();

        for(char ch: s.toCharArray()) {
            if(ch!=' ' && ch!='!' && ch!=',' && ch!='?' && ch!='@' && ch!='_' && ch!='\'' && ch!='.') {
                temp += ch;
            }

            else if(temp.length()>0) {
                result.add(temp);
                temp = "";
            }
        }

        n = result.size();
        System.out.println(n);
        for(String string: result)
            System.out.println(string);



    }
}