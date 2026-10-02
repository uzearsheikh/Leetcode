class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int left =0;
        int curr=0;
        int max = 0;
        int count = 0;
        int n = arr.length;
        for(int right = 0 ; right<n;right++){
            curr += arr[right];
            if(right-left+1 ==k){
                if(curr >= k * threshold){
                    count++;
                    
                }
                curr-=arr[left];
                left++;
            }
       
        
        }
     return count;   
    }
}