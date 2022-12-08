#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    void reverse(vector<int> &nums, int start, int end)
    {
        while (start < end)
        {
            swap(nums[start], nums[end]);
            start++;
            end--;
        }
    }
    void rotate(vector<int> &nums, int k)
    {
        if (k == 0 || nums.size() <= 1)
            return;
        k = k % nums.size();
        int left = 0, right = nums.size() - 1;
        reverse(nums, left, right);
        reverse(nums, left, k - 1);
        reverse(nums, k, right);
    }
};