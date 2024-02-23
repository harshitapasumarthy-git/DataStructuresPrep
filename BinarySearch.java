public class BinarySearch {
    public static int search(int[]arr, int key) {
        int low = 0;
        int high = arr.length-1;
        while(low <= high){
            int mid = low + high/2;
            if(arr[mid]==key){
                System.out.println(mid);
                return mid;
            }
            else if(arr[mid]<key){
                return low = mid+1;
            }
            else{
                return high = mid-1;
            }
            

        }
        System.out.println("Element not found");

       return -1 ;
        
    }
    public static void main(String[] args) {
        int [] arr = {1,3,4,5,6,8};
        int key = 5;
        int res = search(arr,key);
        if (res != -1) {
            System.out.println("Element found at index: " + res);
        } else {
            System.out.println("Element not found");
        }
        
    }
    
}
