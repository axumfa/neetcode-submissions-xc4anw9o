class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        unordered_set<int> cols;
        unordered_set<int> negDiag;
        unordered_set<int> posDiag;
        vector<string> board(n, string(n, '.'));
        vector<vector<string>> res;

        backtrack(0, n, board, res, posDiag, negDiag, cols);

        return res;
    }

    void backtrack(int row, int n, vector<string>& board, vector<vector<string>>& res, unordered_set<int>& posDiag, unordered_set<int>& negDiag, unordered_set<int>& cols)
    {
        if(row == n)
        {
            res.push_back(board);
            return;
        }

        for(int c = 0; c < n; c++)
        {
            if(cols.find(c) != cols.end() || negDiag.find(row - c) != negDiag.end() || posDiag.find(row + c) != posDiag.end())
            {
                continue;
            }

            cols.insert(c);
            negDiag.insert(row - c);
            posDiag.insert(row + c);
            board[row][c] = 'Q';

            backtrack(row + 1, n, board, res, posDiag, negDiag, cols);

            cols.erase(c);
            negDiag.erase(row - c);
            posDiag.erase(row + c);
            board[row][c] = '.';
        }
    }
};