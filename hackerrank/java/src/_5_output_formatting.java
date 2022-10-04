import java.util.*;

public class _5_output_formatting {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        String string;
        int number;

        System.out.println("================================");

        for(int i = 0; i < 3; i++){
            string = input.next();
            number = input.nextInt();
            System.out.printf("%-15s%03d\n", string, number);
        }

        System.out.println("================================");

    }
}
