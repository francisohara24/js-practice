import java.util.Scanner;

public class _0_SampleProblem {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        int N, M;
        int sum;
        for(int i = 1; i <= T; i ++){
            N = input.nextInt();
            M = input.nextInt();
            sum = 0;
            for(int j = 0; j < N; j++)
                sum += input.nextInt();
            System.out.printf("Case #%d: %d\n", i, sum%M);

        }
    }
}