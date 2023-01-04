class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        // define the unordered_map to be of <string ,vector>
        // -key -> string and value -> vector
        unordered_map<string, vector<string>> result;
        for (string &word : strs)
        {
            // the count string will be initialized to have 26 elements
            string count(26, 0);
            for (char &c : s)
            {
                count[c - 'a'] += 1;
            }
            result[count].push_back(word);
        }
        vector<vector<string>> ans;
        for (auto &[key, value] : result)
        {
            ans.push_back(value);
        }
        return ans;
    }
};