import util_java.tree.*;

public class Main {

    static void test(String testName, TreeNode root, boolean expected) {
        var res = new Solution().isSymmetric(root);
        if (res == expected) {
            System.out.println(testName + " success.");
        } else {
            System.out.println(testName + " failed.");
        }
    }

    public static void main(String[] args) {
        //          1
        //         / \
        //        2   2
        //       / \ / \
        //      3  4 4  3
        TreeNode root1 = new TreeNode(1);
        root1.left = new TreeNode(2);
        root1.left.left = new TreeNode(3);
        root1.left.right = new TreeNode(4);
        root1.right = new TreeNode(2);
        root1.right.left = new TreeNode(4);
        root1.right.right = new TreeNode(3);
        boolean expected1 = true;
        test("test1", root1, expected1);

        //          1
        //         / \
        //        2   2
        //       / \ / \
        //         3    3
        TreeNode root2 = new TreeNode(1);
        root2.left = new TreeNode(2);
        root2.left.right = new TreeNode(3);
        root2.right = new TreeNode(2);
        root2.right.right = new TreeNode(3);
        boolean expected2 = false;
        test("test2", root2, expected2);
    }
}

class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return isSym(root.left, root.right);
    }

    private static boolean isSym(TreeNode l, TreeNode r) {
        if (l == null && r == null) {
            return true;
        }
        if (l == null || r == null) {
            return false;
        }
        if (l.val != r.val) {
            return false;
        }
        return isSym(l.left, r.right) && isSym(l.right, r.left);
    }
}
