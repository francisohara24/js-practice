import java.util.Scanner;

public class _1_CentauriPrime {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        String kingdom;
        String owner;
        String vowels = "aeiouAEIOU";

        for(int i = 1; i <= T; i++){
            owner = "Bob";
            kingdom = input.next();

            if(kingdom.charAt(kingdom.length()-1)=='Y' || kingdom.charAt(kingdom.length()-1)=='y')
                owner = "nobody";
            else
                for(char vowel: vowels.toCharArray())
                    if (vowel==kingdom.charAt(kingdom.length()-1)){
                        owner = "Alice";
                        break;
                    }

            System.out.printf("Case #%d: %s is ruled by %s.\n", i, kingdom,owner);
        }
    }

}