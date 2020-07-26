学习笔记
1、问题的分析归纳总结很重要
2、递归 Recursion
def recursion(level, param1, param2, ...):
	# recursion terminator
	if level > MAX_LEVEL:
		process_result
		return
		
	# process logic in current level
	process(level, data, ...)
	
	# drill down
	self,recursion(level + 1, p1, ...)
	
	# reverse the current level status if needed
思维要点：
1、不要人肉递归
2、找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3、数学归纳法思维

3、分治 Divide & Conquer
def divide_conquer(problem, param1, param2, ...):
	# recursion terminator
	if problem is None:
		print_result
		return
		
	# prepare data
	data = prepare_data(problem)
	subproblems = split_problem(problem, data)
	
	# conquer subproblems
	subresult1 = self.divide_conquer(subproblems[0], p1, ...)
	subresult2 = self.divide_conquer(subproblems[1], p1, ...)
	subresult3 = self.divide_conquer(subproblems[2], p1, ...)
	...
	
	# process and generate the final result
	result = process_result(subresult1, subresult2, subresult3, ...)
	
	# revert the current level status

当前层只做当前层需要做的事情，尽量不要做其他层的事情。	