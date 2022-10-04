import java.util.*;

public class _3_java_if_else {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();

        if (n%2==1)
            System.out.println("Weird");
        else if (n>=2 && n <= 5)
            System.out.println("Not Weird");
        else if (n>=6 && n <= 20)
            System.out.println("Weird");
        else
            System.out.println("Not Weird");
    }
}
