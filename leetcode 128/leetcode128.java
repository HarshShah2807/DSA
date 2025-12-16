class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length==0) return 0;
        Set<Integer> setnums = new HashSet<>();
        for (int num : nums) {
            setnums.add(num);
        }
        int best=0;
        for (int i:setnums){
            if(!setnums.contains(i-1)){
                int length = 1;
                while(setnums.contains(i+length)) length++;
                best=Math.max(best,length);
            }
        }
        return best;
    }
}
