class Solution {
public:
    unordered_set<int> visits;
    unordered_map<int, unordered_set<int>> adj;

    int countComponents(int n, vector<vector<int>>& edges) {
            // logic to find full number of vertex in graph and compare it with adjency listy
        for(auto pair : edges)
        {
            int num1 = pair[0];
            int num2 = pair[1];

            adj[num1].insert(num2);
            adj[num2].insert(num1);
        }       
        int ans = 0;

        for(int i = 0; i < n; i++)
        {
            if(visits.count(i))
                continue;
                
            vector<int> temp;
            dfs(i, temp);
            bool flag = true;

            for(int v : temp)
            {   if(temp.size() - 1 != adj[v].size())
                    flag = false;
            }
            if(flag)
                ans++;
        }
        return ans;
    }

    void dfs(int v, vector<int> res)
    {
        if(visits.count(v))
            return;
        
        visits.insert(v);
        res.push_back(v);

        for(int neigh : adj[v])
            dfs(neigh, res);
    }
};
