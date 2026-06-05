import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class Main {
    public static int partition(List<Integer> nums, int low, int high) {
        int pivot = nums.get(high);
        int i = low - 1;
        for(int j = low; j < high; j++) {
            if(nums.get(j) <= pivot) {
                int temp = nums.get(j);
                nums.set(j, nums.get(i + 1));
                nums.set(i + 1, temp);
                i++;
            }
        }
        if((i+1) != high) {
            int temp = nums.get(i + 1);
            nums.set(i + 1, nums.get(high));
            nums.set(high, temp);
        }
        return i + 1;
    }
    public static void sort(List<Integer> nums, int low, int high) {
        if(low >= high){
            return;
        }
        int pi = partition(nums, low, high);
        sort(nums, low, pi - 1);
        sort(nums, pi + 1, high);
    }
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>();
        int n = sc.nextInt();
        for(int I = 0; I < n; I++) {
            int num = sc.nextInt();
            nums.add(num);
        }
        sort(nums, 0, n - 1);
        for(int I = 0; I < n; I++) {
            if(I == (n-1)) {
                System.out.print(nums.get(I));
            } else {
                System.out.print(nums.get(I) + " ");
            }
        }
    }
}
