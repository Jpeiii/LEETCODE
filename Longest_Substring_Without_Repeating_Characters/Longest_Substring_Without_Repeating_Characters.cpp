class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        set<char> subStringSet;
        int left = 0;
        int longestSubString = 0;
        for (int right = 0; right < s.size(); right++)
        {
            while (subStringSet.find(s[right]) != subStringSet.end())
            {
                subStringSet.erase(s[left]);
                left++;
            }
            subStringSet.insert(s[right]);
            longestSubString = max(longestSubString, right - left + 1);
        }
        return longestSubString;
    }
};