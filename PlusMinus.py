def plusMinus(arr):
	n = len(arr)
	pos = sum(x>0 for x in arr)
	neg = sum(x<0 for x in arr)
	zero = sum(x == 0 for x in arr)
	print("{:.6f}".format(pos/n))
	print("{:.6f}".format(neg/n))
	print("{:.6f}".format(zero/n))
	
n = int(input())
arr = list(map(int, input().split()))
plusMinus(arr)