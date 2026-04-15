class TrieNode
{
public:
    TrieNode* children[26];
    bool isEnd = false; 
    TrieNode()
    {
        nullFunc();
    }
void nullFunc()
{
    for(int i = 0; i < 26; i++)
    {
        this->children[i] = nullptr;
    }
}

};


class WordDictionary {
public:
    TrieNode* root;
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* cur = root;

        for(auto c : word)
        {
            int idx = c - 'a';
            if(cur->children[idx] == nullptr)
            {
                cur->children[idx] = new TrieNode();
            }
            cur = cur->children[idx];
        }
        cur->isEnd = true;
    }

    bool dfs(int j, TrieNode* cur, string word)
    {
        TrieNode* node = cur;
        int length = word.length();

        for(int i = j; i < length; i++)
        {
            char c = word[i];
            if(c == '.')
            {
                for(int k = 0; k < 26; k++)
                {
                    if(cur->children[k] == nullptr)
                        continue;
                    TrieNode* child = cur->children[k];
                    if(dfs(i + 1, child, word))
                        return true;
                }
                return false;
            }
            else
            {
                int idx = word[i] - 'a';
                if(cur->children[idx] == nullptr)
                    return false;
                cur = cur->children[idx];
            }
        
        }
        return cur->isEnd;
    }
    
    bool search(string word) {
        return dfs(0, root, word);
    }
};
