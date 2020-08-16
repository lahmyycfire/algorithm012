学习笔记
1.递归代码模板 
def recursion(level, param1, param2, ...): 
# recursion terminator 
if level > MAX_LEVEL: process_result return 
# process logic in current level 
process(level, data...) 
# drill down 
self.recursion(level + 1, p1, ...) 
# reverse the current level status if needed



2.动态规划关键点 
(1)最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], ...) 
(2)储存中间状态：opt[i] 
(3)递推公式（状态转移方程或者DP方程） Fib: opt[i]=opt[n-1]+opt[n-2] 二维路径：opt[i,j]=opt[i+1][j]+opt[i][j+1] （判断a[i.j]是否空地）