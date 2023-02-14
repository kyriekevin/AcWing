class Solution {
public:
    int duplicateInArray(vector<int>& nums) {
        int n = nums.size();
        for (int num: nums)
            if (num < 0 || num > n - 1)
                return -1;
        for (int i = 0; i < n; i++) {
            while (nums[nums[i]] != nums[i]) 
                swap(nums[i], nums[nums[i]]);
            if (nums[i] != i)
                return nums[i];
        }
        
        return -1;
    }
};
