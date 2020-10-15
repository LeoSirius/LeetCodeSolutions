import java.io.*;
import java.util.*;

import util_java.tree.*;

public class Main {
    public static void main(String[] args) {
        //    3
        //   / \
        //  1   4
        //   \
        //    2
        TreeNode root1 = new TreeNode(3);
        root1.left = new TreeNode(1);
        root1.left.right = new TreeNode(2);
        root1.right = new TreeNode(4);
        int k1 = 1;
        int expected1 = 4;
        test("test1", root1, k1, expected1);


        //        5
        //       / \
        //      3   6
        //     / \
        //    2   4
        //   /
        //  1
        TreeNode root2 = new TreeNode(5);
        root2.left = new TreeNode(3);
        root2.left.left = new TreeNode(2);
        root2.left.right = new TreeNode(4);
        root2.left.left.left = new TreeNode(1);
        root2.right = new TreeNode(6);
        int k2 = 3;
        int expected2 = 4;
        test("test2", root2, k2, expected2);
    }

    static void test(String testName, TreeNode root, int k, int expected) {
        int res = new Solution().kthLargest(root, k);
        if (res == expected) {
            System.out.println(testName + " success.");
        } else {
            System.out.println(testName + " failed.");
        }
    }
}

class Solution {
    public int kthLargest(TreeNode root, int k) {
        TreeNode p = root;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        int cnt = 0;
        while (stk.size() > 0 || p != null) {
            while (p != null) {
                stk.push(p);
                p = p.right;
            }
            p = stk.pop();
            cnt++;
            if (cnt == k) {
                return p.val;
            }
            p = p.left;
        }
        return 0;
    }
}

//  给定一棵二叉搜索树，请找出其中第k大的节点。

//  限制：
//  1 ≤ k ≤ 二叉搜索树元素个数
