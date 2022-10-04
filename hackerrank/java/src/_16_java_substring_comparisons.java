import java.util.ArrayList;

public class _16_java_substring_comparisons {

    public static void main(String[] args){

        String s = "welcometojava";
        int k = 3;
        ArrayList<String> substrings = new ArrayList<>();

        for(int i = 0; i<= s.length()-k; i++)
            substrings.add(s.substring(i, i+k));

        String largest = substrings.get(0);
        String smallest = substrings.get(0);

        for (String substring : substrings) {
            if (largest.compareTo(substring) < 0)
                largest = substring;
            if (smallest.compareTo(substring) > 0)
                smallest = substring;
        }

        System.out.println(smallest + "\n" + largest);

    }
}
