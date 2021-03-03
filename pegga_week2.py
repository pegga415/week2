#題目一：在函式中​使用迴圈​計算最小值到最大值之間，所有整數的總和。
def calculate(min,max):
	sum = 0
	for x in range(min,max+1):
		sum += x
	print(sum)

calculate(1,3)
calculate(4,8)

#題目二：完成以下函式，正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
def avg(data):
	count = data['count']
	sum = 0
	for x in range(count):
		sum += data['employees'][x]['salary']
	print(sum/count)

avg({
"count":3, 
"employees":[
		{
			"name":"John",
			"salary":30000 
		},
		{
			"name":"Bob",
			"salary":60000 
		},
		{
			"name":"Jenny",
			"salary":50000 
		}
	]
})

#題目三：找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
def maxProduct(nums):
	result = []
	for x in range(len(nums)-1):
		for y in range(x+1,len(nums)):
			result += [nums[x]*nums[y]]
	t = 0
	for n in range(len(result)):
		if t < result[n]:
			t = result[n]
	print(t)

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])

#題目四：
def twoSum(nums,target):
	for x in range(len(nums)-1):
		for y in range(1,len(nums)):
			s = nums[x] + nums[y]
			if s == target:
				return [x,y]

result = twoSum([2,11,7,15],9)
print(result)


#題目五：給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。
def maxZeros(nums):
	zero = []
	count = 0
	for x in range(len(nums)):
		if nums[x] == 0:
			count += 1
			if x == len(nums)-1:
				zero += [count]
		else:
			zero += [count]
			count = 0
	t = 0
	for y in range(len(zero)):
		if t < zero[y]:
			t = zero[y]
	print(t)		

maxZeros([0,1,0,0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])