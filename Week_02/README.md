学习笔记 week02

1、二叉树
# 定义
def __init__(self, val):
	self.val = val
	self.left, self.right = None, None

# 前序遍历
def preorder(self, root):
	if root:
		self.traverse_path.append(root.val)
		self.preorder(root.left)
		self.preorder(root.right)

# 中序遍历
def inorder(self, root):
	if root:
		self.inorder(root.left)
		self.traverse_path.append(root.val)
		self.inorder(root.right)

# 后序遍历
def postorder(self, root):
	if root:
		self.postorder(root.left)
		self.postorder(root.right)
		self.traverse_path.append(root.val)
		

# 迭代：前、中、后序遍历通用模板（只需一个栈的空间）
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        
        # # 前序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res
        
        # # 后序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     cur = stack.pop()
        #     cur = cur.left
        # return res[::-1]
		
		
2、堆 heap
Heap: 可以迅速的找到一堆数中最大或者最小的值的数据结构
根节点最大：大顶堆、大跟堆
根节点最小：小顶堆、小跟堆
常见的有二叉堆（容易实现，效率相对不高）、斐波拉契堆（效率高）等

二叉树（大顶）满足下列性质：
【1】是一颗完全二叉树
【2】树中任意节点的值总是>=其子节点的值

二叉树一般都通过“数组”来实现
【1】索引为i的左孩子的索引是(2*i + 1)
【2】索引为i的右孩子的索引是(2*i + 2)
【3】索引为i的父节点的索引是floor((i - 1)/2);

insert: HeapifyUp
delete: HeapifyDown
 (二叉堆insert和delete一个元素之后，就不是二叉堆了？因为不满足第一个条件？）
 
3、看官方源代码，学习简洁的代码

4、7月18号leetcode的每日一题：给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
第一思路是遍历s3,存到dict中，然后遍历s1,减去相应字母在dict中的数量，最后得到的字符串与s2比较，但是这种方法对于有些测试用例是不行的。
官方题解中用的是动态规划，要多培养自己的思路，这类题目确实是要用动态规划，不能用常规的写法。
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if "" in (s1, s2):
            return s3 in (s1, s2)   # 空值处理
        len1, len2 = len(s1), len(s2)
        if len1+len2 != len(s3):
            return False  # 长度限定（同时也防止s3下标越界）
        minj = 0
        maxj = [c1 == c2 for c1, c2 in zip(s2+'$', s3)].index(False)
        dp = [True]*(maxj+1) + [False]*(len2-maxj)  # 首行
        # 遍历完成后： dp[j] == isInterleave(s1,s2[:j],s3[len1+j:])
        for i in range(len1):
            while (minj <= maxj) and (not dp[minj]):
                minj += 1
            if minj > maxj: return False
            dp[minj] = s1[i] == s3[i+minj]
            for j in range(minj, maxj):
                dp[j+1] = (dp[j+1] and s1[i] == s3[i+j+1]) or (dp[j] and s2[j] == s3[i+j+1])
            while maxj < len2 and dp[maxj] and s2[maxj] == s3[i+maxj+1]:
                maxj += 1
                dp[maxj] = True
        return dp[-1]
        