class TrieNode
{

public:
    TrieNode* children[26];
    bool isEnd = false;

    void nullFunc()
    {
        for(int i = 0; i < 26; i++)
        {
            this->children[i] = nullptr;
        }
    }

    TrieNode()
    {
        nullFunc();
    }
};

class PrefixTree {
public:
    TrieNode* root;
    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* cur = root;
        

        for(auto c : word)
        {
            int index = c - 'a';
            if(cur->children[index] == nullptr)
            {
                cur->children[index] = new TrieNode();
            }
            cur = cur->children[index];
        }
        cur->isEnd = true;
    }
    
    bool search(string word) {
        TrieNode* cur = root;
        int length = sizeof(word);

        for(auto c : word)
        {
            int index = c - 'a';
            if(cur->children[index] == nullptr)
            {
                return false;
            }
            cur = cur->children[index];
        }
        return cur->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root;
                for(auto c : prefix)
        {
            int index = c - 'a';
            if(cur->children[index] == nullptr)
            {
                return false;
            }
            cur = cur->children[index];
        }
        return true;
    }
};
