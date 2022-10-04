import java.util.regex.Pattern;
import java.util.Scanner;

public class _21_java_regex {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Pattern pattern1 = Pattern.compile(MyRegex.pattern);

        while(input.hasNextLine()){
            String s = input.next();
            System.out.println(Pattern.matches(MyRegex.pattern, s));
        }


    }
}

class MyRegex {
        static String pattern = "([0-9]|[0-9][0-9]|[0-2][0-5][0-5]|[1-2][0-4][0-9]).([0-9]|[0-9][0-9]|[0-2][0-5][0-5]|[1-2][0-4][0-9]).([0-9]|[0-9][0-9]|[0-2][0-5][0-5]|[1-2][0-4][0-9]).([0-9]|[0-9][0-9]|[0-2][0-5][0-5]|[1-2][0-4][0-9])";
}