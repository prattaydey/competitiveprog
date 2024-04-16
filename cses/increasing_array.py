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
    n = int(input())
    a = list(map(int, input().split()))
    min_moves = 0
    for i in range(1,n):
    	if a[i] < a[i - 1]:
    		min_moves += a[i - 1] - a[i]
    		a[i] = a[i - 1]
    print(min_moves)
    		

            
if __name__ == "__main__":
    t = 1
    # t = int(input())
    while t > 0:
    	main()
    	t -= 1


