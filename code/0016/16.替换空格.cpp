class Solution {
public:
  string replaceSpaces(string &str) {
    int len = 0;
    for (auto ch : str)
      if (ch == ' ')
        len += 3;
      else
        len++;

    int i = str.size() - 1, j = len - 1;
    str.resize(len);

    while (i >= 0) {
      if (str[i] == ' ') {
        str[j--] = '0';
        str[j--] = '2';
        str[j--] = '%';
      } else
        str[j--] = str[i];
      i--;
    }

    return str;
  }
};
