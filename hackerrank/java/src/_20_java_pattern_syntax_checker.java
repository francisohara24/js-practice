import java.util.*;
import java.util.regex.*;

public class _20_java_pattern_syntax_checker {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        input.nextLine();
        for(int i = 0; i < N; i ++) {
            try{
                Pattern.compile(input.nextLine());
                System.out.println("Valid");
            } catch(PatternSyntaxException e){
                System.out.println("Invalid");
            }
        }
    }
}
