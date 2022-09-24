import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result1 {

    /*
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) {
        int target = arr.get(arr.size() - 1);
        for (int i = arr.size() - 1; i >= 0; i--) {
            if (i != 0) {
                if (arr.get(i - 1) < target) {
                    arr.set(i, target);
                    for (int j : arr)
                        System.out.print(j + " ");
                    break;
                } else {
                    arr.set(i, arr.get(i - 1));
                    for (int j : arr)
                        System.out.print(j + " ");
                    System.out.println();
                }
            }
            else {
                arr.set(i, target);
                for (int j : arr)
                    System.out.print(j + " ");

            }
        }
    }

}

public class _1_InsertionSortPart1 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        Result1.insertionSort1(n, arr);

        bufferedReader.close();
    }
}
