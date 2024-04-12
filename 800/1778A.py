for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	sum = 0
	for i in range(len(a)):
		sum += a[i]
	status = False
	for j in range(n-1):
		if a[j] == a[j+1] and a[j] == -1:
			sum += 4
			break
		elif a[j] != a[j+1]:
			status = True
	if not status:
		if a[j] == a[j+1] and a[j] == 1:
			sum -= 4
	print(sum)
