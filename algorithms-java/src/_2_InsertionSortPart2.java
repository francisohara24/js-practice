import java.util.List;

public class _2_InsertionSortPart2 {
    public static void arrPrint(List<Integer> arr){
        for (int value: arr) System.out.print(value + " ");
    }

    public static void insertionSort2(int n, List<Integer> arr){
        for (int i = 1; i < n; i ++){
            int target = arr.get(i);
            for (int j = i; j >= 0; j--){
                if (j==0){
                    arr.set(j, target);
                    arrPrint(arr);
                    System.out.println();
                }
                else if (arr.get(j-1) < target) {
                    arr.set(j, target);
                    arrPrint(arr);
                    System.out.println();
                }
                else
                    arr.set(j, arr.get(j-1));

            }
        }
    }
}
