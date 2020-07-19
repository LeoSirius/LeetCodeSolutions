#include <stdio.h>
#include "./utils_c/tree.h"


typedef struct TreeNode element_type;

struct stack_record {
    int capacity;
    int top_of_stack;
    element_type *array;
};

typedef struct stack_record *stack;

stack new_stack(int size);
int is_empty(stack stk);
int is_full(stack stk);
void del_stack(stack stk);
void make_empty(stack stk);
void push(stack stk, element_type x);
void pop(stack stk);
element_type top(stack stk);

void expand(stack stk);


stack new_stack(int size)
{
    stack stk;
    stk = (stack)malloc(sizeof(struct stack_record));
    if (stk == NULL) {
        printf("This is %s() from %s, line %d\n", __FUNCTION__, __FILE__, __LINE__);
        printf("malloc error\n");
        return NULL;
    }
    stk->array = malloc(sizeof(element_type) * size);
    if (stk->array == NULL) {
        printf("This is %s() from %s, line %d\n", __FUNCTION__, __FILE__, __LINE__);
        printf("malloc error\n");
        return NULL;
    }

    stk->capacity = size;
    make_empty(stk);

    return stk;
}

void make_empty(stack stk)
{
    if (stk == NULL) return;
    stk->top_of_stack = -1;
}

void del_stack(stack stk)
{
    if (stk == NULL) return;
    free(stk->array);
    free(stk);
}

void push(stack stk, element_type x)
{
    if (is_full(stk)) {
        expand(stk);
    }

    stk->array[++stk->top_of_stack] = x;
}

element_type top(stack stk)
{
    if (is_empty(stk)) {
        // todo: log info
        return 0;  // return a value to avoid warning
    }
    return stk->array[stk->top_of_stack];
}

void pop(stack stk)
{
    if (is_empty(stk)) {
        // todo : log
        return 0;
    }
    --stk->top_of_stack;
}

int is_full(stack stk)
{
    return stk->top_of_stack == stk->capacity - 1;
}

int is_empty(stack stk)
{
    return stk->top_of_stack == -1;
}

void expand(stack stk)
{
    stk->capacity *= 2;
    realloc(stk->array, stk->capacity);
}


int kthLargest(struct TreeNode* root, int k){

}

void test(char *test_name, struct TreeNode *root, int k, int expected)
{
    int res = kthLargest(root, k);
    if (res == expected)
        print("%s success", test_name);
    else
        print("%s failed", test_name);
}

int main()
{

    //   3
    //  / \
    // 1   4
    //  \
    //   2
    struct TreeNode *root1 = new_tree_node(3);
    root1->left = new_tree_node(1);
    root1->left->right = new_tree_node(2);
    root1->right = new_tree_node(4);
    int k1 = 1;
    int expected1 = 4;

    //         5
    //        / \
    //       3   6
    //      / \
    //     2   4
    //    /
    //   1
    return 0;
}

// 给定一棵二叉搜索树，请找出其中第k大的节点。

// 限制：
// 1 ≤ k ≤ 二叉搜索树元素个数