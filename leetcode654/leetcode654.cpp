/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        if (nums.empty()) return nullptr;
        auto max_iter = max_element(nums.begin(), nums.end());
        int max_val = *max_iter;
        int max_idx = distance(nums.begin(), max_iter);
        TreeNode* root = new TreeNode(max_val);
        vector<int> left(nums.begin(), nums.begin() + max_idx);
        vector<int> right(nums.begin() + max_idx + 1, nums.end());
        root->left = constructMaximumBinaryTree(left);
        root->right = constructMaximumBinaryTree(right);
        return root;
    }
};
