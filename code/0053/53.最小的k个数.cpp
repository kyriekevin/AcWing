class Solution {
public:
    vector<int> getLeastNumbers_Solution(vector<int> input, int k) {
        sort(input.begin(), input.end());
        input.resize(k);
        return input;
    }
};
