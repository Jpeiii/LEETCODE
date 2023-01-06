class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        subStringSet = set()
        longestSubString = 0
        for right in range(len(s)):
            while s[right] in subStringSet:
                subStringSet.remove(s[left])
                left += 1
            subStringSet.add(s[right])
            longestSubString = max(longestSubString, right-left+1)
        return longestSubString
