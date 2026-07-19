/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        func(root, val);
        return root;
    }

    void func(TreeNode*& root, int val)
    {
        if(!root)
        {   
            root = new TreeNode(val);
            return;
        }
        if(root->val > val)
            func(root->left, val);
        else
            func(root->right, val);
    }
};