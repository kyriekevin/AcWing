class Solution {
public:
  bool searchArray(vector<vector<int>> array, int target) {
    if (array.empty())
      return false;
    int n = array.size(), m = array[0].size();
    for (int i = 0, j = m - 1; i < n && j >= 0;) {
      if (array[i][j] > target)
        j--;
      else if (array[i][j] < target)
        i++;
      else
        return true;
    }

    return false;
  }
};
