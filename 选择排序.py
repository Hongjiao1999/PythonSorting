array = [61, 65, 46, 51, 23, 18, 48, 45, 13, 21, 86, 49, 84, 32, 1]

def 选择排序(要排序的数组):
	for i in range(len(要排序的数组) - 1):
		当前最小数的索引 = i
		for j in range(i + 1, len(要排序的数组)):
			if 要排序的数组[j] < 要排序的数组[当前最小数的索引]:
				当前最小数的索引 = j
		if i != 当前最小数的索引:
			要排序的数组[i], 要排序的数组[当前最小数的索引] = 要排序的数组[当前最小数的索引], 要排序的数组[i]
	return 要排序的数组

'''
	j < 当前索引（此时索引意义为当前最小数） 表示升序排列，j > 当前索引（此时索引意义为当前最大数） 表示降序排列
'''
print(选择排序(array))
