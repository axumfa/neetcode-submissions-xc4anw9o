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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root)
            return nullptr;

        if(root->val > key)
            root->left = deleteNode(root->left, key);
        else if(root->val < key)
            root->right = deleteNode(root->right, key);

        else{
            if(!root->left && !root->right)
            {
                delete root;
                return nullptr;
            }
            else if(!root->left)
            {
                TreeNode* tmp = root->right;
                delete root;
                return tmp;
            }
            else if(!root->right)
            {
                TreeNode* tmp = root->left;
                delete root;
                return tmp;
            }

            TreeNode *pred = findMax(root->left);

            root->val = pred->val;

            root->left = deleteNode(root->left, pred->val);
        }
        return root;
            
    }
    // I want to left sides max
    TreeNode* findMax(TreeNode* node)
    {
        while(node->right)
            node = node->right;
        return node;
    }
};