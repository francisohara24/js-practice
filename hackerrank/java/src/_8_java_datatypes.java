import java.util.*;

public class _8_java_datatypes {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        String numberString = "";
        long number;

        for(int i=0; i< T;i++){
            try{
                numberString = input.next();
                number = Long.parseLong(numberString);
                System.out.println(numberString + " can be fitted in:");
                if(number >= Byte.MIN_VALUE && number <= Byte.MAX_VALUE)
                    System.out.println("* byte");
                if (number >= Short.MIN_VALUE && number <= Short.MAX_VALUE)
                    System.out.println("* short");
                if (number >= Integer.MIN_VALUE && number <= Integer.MAX_VALUE)
                    System.out.println("* int");
                System.out.println("* long");

            } catch(NumberFormatException e) {
                System.out.println(numberString + " can't be fitted anywhere.");
            }

        }
    }
}
