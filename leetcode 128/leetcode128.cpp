class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        unordered_set<int> setnums(nums.begin(),nums.end());
        int best=0;
        for (int i:setnums){
            if (setnums.find(i - 1) == setnums.end()) {
                int length=1;
                while (setnums.find(i+length)!=setnums.end()) length++;
                best=max(best,length);
            }    
        }
    return best;    
    }
};
