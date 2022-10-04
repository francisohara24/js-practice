import java.util.*;

public class _7_java_loops_II {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner input = new Scanner(System.in);
        int q = input.nextInt();
        int a, b, n, currentTerm, previousTerm;

        for(int i = 0; i < q; i++){
            a = input.nextInt();
            b = input.nextInt();
            n = input.nextInt();
            previousTerm = a;

            for(int j = 0; j < n; j++){
                currentTerm = previousTerm + ((int) Math.pow(2, j) * b);
                System.out.print(currentTerm + " ");
                previousTerm = currentTerm;
            }
            System.out.println();
        }


    }
}
