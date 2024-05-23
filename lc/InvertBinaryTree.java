package lc;

public class InvertBinaryTree {

    public static TreeNode invertTree(TreeNode root) {
        TreeNode temp;
        if (root == null) {
            return root;
        }

        temp = root.left;
        root.left = root.right;
        root.right = temp;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
        return root;

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        invertTree(root);
        System.out.println("Val: " + root.val);
    }
}
