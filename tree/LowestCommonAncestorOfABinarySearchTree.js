/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
// INCLUSIVE
const isInBetween = (val, p, q) => (val >= Math.min(p, q)) && (val <= Math.max(p, q));

 /**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
const lowestCommonAncestor = (root, p, q) => {
  if (!root) return;
  // Always the first between
  if (isInBetween(root.val, p.val, q.val)) return root;
  if (root.val < Math.min(p.val, q.val)) return lowestCommonAncestor(root.right, p, q);
  if (root.val > Math.max(p.val, q.val)) return lowestCommonAncestor(root.left, p, q);
  // LCA does not exist
};
