class Solution {
public:
    int getNumberOfK(vector<int>& nums , int k) {
        int l = lower_bound(nums.begin(), nums.end(), k) - nums.begin();
        int r = upper_bound(nums.begin(), nums.end(), k) - nums.begin();
        return r - l;
    }
};
