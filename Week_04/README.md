学习笔记
1、二分查找（单调、边界、Index）
left, right = 0, len(array) - 1
while left < right:
	mid = (right + left)/2
	if array[mid] == target:
		return result
	elif array[mid] < target:
		left = mid + 1
	else:
		right = mid - 1
	
2、贪心算法：局部最优值累计得到结果最优，和动态规划区别是，贪心算法不保存历史记录不能回退，没有回溯，而动态规划保存历史记录。
贪心方向可以是从头开始、从尾开始。

3、dfs
-- 二叉树
def dfs(node):
	if node in visited:
		# already visited
		return 
	
	visited.add(node)
	
	# process current node
	# ... # logic here
	dfs(node.left)
	dfs(node.right)

-- 多叉树
visited = set()

def dfs(node, visited):
	visited.add(node)
	# process current node here
	...
	for next_node in node.children():
		if not next_node in visited:
			dfs(next_node, visited)
			
-- 非递归写法
def dfs_stack(self, tree):
	if tree.root is None:
		return []
	
	visited, stack = [], [tree.root]
	while stack:
		node = stack.pop()
		visited.add(node)
		
		process(node)
		nodes = generate_related_nodes(node)
		stack.push(nodes)
		
		
4、bfs
def bfs(graph, start, end):
	queue = []
	queue.append([start])
	
	visited.add(start)
	
	while queue:
		node = queue.pop()
		visited.add(node)
		
		process(node)
		nodes = generate_related_nodes(node)
		queue.push(nodes)
		
-- binary_search
def binary_search(array, target):
	left, right = 0, len(array) - 1
	while left<= right:
		mid = (right + left) / 2
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			left = mid + 1
		else:
			right = mid -1 
	