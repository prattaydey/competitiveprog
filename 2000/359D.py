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
	n = int(input()) + 1
	a = [1] + list(map(int, input().split())) + [1] # added buffers 
for while loop
	visited = [False] * n
	longest = 0
	start = list(range(1,n))
	
	for i in range(1,n):
		if visited[i] == False:
			# initializes left and right boundary at index i
			l, r = i, i
			divisor = a[i]
			
			# if 1, then can divide the whole array
			if divisor == 1:
				longest = n - 2
				start = [1]
				break
			# else, expand left and right outwards
			while a[l - 1] % divisor == 0:
				l -= 1
			while a[r + 1] % divisor == 0:
				r += 1
				visited[r] = True
				
			length = r - l
			# if current seg is larger
			if length > longest:
				longest = length
				start = [l] # restart our starting points
				
			# if current seg is same
			elif length == longest and length != 0:
				start.append(l) 
				
	print(len(start), longest) # num of pairs, length of longest 
segment
	print(*start) # starting point of each pair
				
			
	
			
if __name__ == "__main__":
	t = 1
	# t = int(input())
	while t > 0:
		main()
		t -= 1
