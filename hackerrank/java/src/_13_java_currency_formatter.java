import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class _13_java_currency_formatter {
    public static void main(String[] args) {
        NumberFormat usFormatter = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat chinaFormatter = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat franceFormatter = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        NumberFormat indiaFormatter = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));

        Scanner input = new Scanner(System.in);
        double payment = input.nextDouble();

        String u = usFormatter.format(payment);
        String i = indiaFormatter.format(payment);
        String c = chinaFormatter.format(payment);
        String f = franceFormatter.format(payment);

        System.out.println("US: " + u);
        System.out.println("India: " + i);
        System.out.println("China: " + c);
        System.out.println("France: " + f);

    }
}
