import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict, Counter
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: i4nt(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007
        
def main():
	n, m = map(int, input().split())
	# 2D array storing endpoint for segment opening at index i
	open = [[] for _ in range(n+1)] 
	# num of segments ending at index i
	close = [0] * (n + 1)
	# num of segments active at index i
	active = [0] * (n + 1)
	
	# processing inputs and building our arrays
	for _ in range(m):
		l, r = map(int, input().split())
		l -= 1 # 0 indexing
		open[l].append(r)
		close[r] += 1
		
	# will keep track of the num of active segments at current index
	curr = 0 
	# will be used to determine our rightmost boundary x
	max_end = -1
	g = [0] * (n + 1)
	
	for i in range(n + 1):
		for x in open[i]:
			curr += 1
			max_end = max(max_end, x)
		curr -= close[i]
		active[i] = curr
		g[i] = max(max_end, i + 1) # determines value x to jump to
	
	dp = [0] * (n + 1)
	dp[0] = 0
	
	for i in range(n):
		dp[i + 1] = max(dp[i + 1], dp[i])
		if g[i] <= n:
			dp[g[i]] = max(dp[g[i]], dp[i] + active[i])
			
	print(dp[n])
    

            
if __name__ == "__main__":
    t = 1
    t = int(input())
    while t > 0:
    	main()
    	t -= 1


