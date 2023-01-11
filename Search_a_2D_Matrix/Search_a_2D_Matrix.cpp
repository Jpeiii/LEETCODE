class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int ROWS = matrix.size();
        int COLS = matrix[0].size();
        int top = 0;
        int bottom = ROWS - 1;

        while (top < bottom)
        {
            int medianRow = top + (bottom - top) / 2;
            if (target > matrix[medianRow][0])
            {
                top = medianRow + 1;
            }
            else
            {
                bottom = medianRow - 1;
            }

            if (matrix[medianRow][0] == target)
            {
                return true;
            }

            if (target > matrix[medianRow][0] && target < matrix[medianRow + 1][0])
            {
                top = medianRow;
                break;
            }
        }
        int left = 0;
        int right = COLS - 1;
        while (left <= right)
        {
            int medianCols = left + (right - left) / 2;
            if (matrix[top][medianCols] == target)
            {
                return true;
            }
            if (target > matrix[top][medianCols])
            {
                left = medianCols + 1;
            }
            else
            {
                right = medianCols - 1;
            }
        }
        return false;
    }
};