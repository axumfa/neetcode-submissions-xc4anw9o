
class Solution {
public:
  void bfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int r, int c) {
    queue<pair<int, int>> q;
    int r_limit = visited.size();
    int c_limit = visited[0].size();
    q.push({r, c});

    while (q.size() > 0) {
      auto [row, col] = q.front();
      q.pop();
      vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

      for (auto[dr, dc] : directions) {
        int rl = row + dr;
        int cl = col + dc;
           if (rl >= 0 && rl < r_limit && cl >= 0 && cl < c_limit && !visited[rl][cl] && grid[rl][cl] == '1')
           {
            visited[rl][cl] = 1;
            q.push({rl, cl});
           }
        
           
      }
    }
  }
  int numIslands(vector<vector<char>> &grid) {
    int r = grid.size();
    int c = grid[0].size();
    int islands = 0;
  vector<vector<bool>> visited(r, vector<bool>(c, false));

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (grid[i][j] == '1' && !(visited[i][j]))
        {
          bfs(grid, visited, i, j);
          islands++;
          visited[i][j] = 1;
        }
      }
    }
    return islands;
  }
};


