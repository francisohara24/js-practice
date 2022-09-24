import java.util.List;

public class _1_InsertionSortPart1{

    public static void insertionSort1(int n, List<Integer> arr){
        int target = arr.get(arr.size()-1);
        for (int i = arr.size() - 1; i >= 0; i --){
            if (arr.get(i) <= target) {
                arr.set(i, target);
                break;
            }
            else {
                arr.set(i, arr.get(i-1));
            }
        }
    }




}