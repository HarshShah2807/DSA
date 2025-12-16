/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return build(nums, 0, nums.length);
    }

    private TreeNode build(int[] nums, int start, int end) {
        if (start >= end) return null;
        int maxIdx = start;
        for (int i = start; i < end; i++) {
            if (nums[i] > nums[maxIdx]) {
                maxIdx = i;
            }
        }
        TreeNode root = new TreeNode(nums[maxIdx]);
        root.left = build(nums, start, maxIdx);
        root.right = build(nums, maxIdx + 1, end);
        return root;
    }
}
