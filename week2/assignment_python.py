# 要求一
def calculate(min, max, step):
   total = 0
   for num in range(min, max+1, step):
       total += num
   print(total)
calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)
print("---------------------------")

# 要求二
def avg(data):
   data = data["employees"]
   newdata=[]
   for i in data:
       if i["manager"] == True:
           continue
       newdata.append(i)
 
   sum = 0
   avg = 0
   for n in newdata:
       sum += n["salary"]
 
   avg = sum / len(newdata)
   print(int(avg))
 
avg({
   "employees":[
       {
       "name":"John",
       "salary":30000,
       "manager":False
       },
       {
       "name":"Bob",
       "salary":60000,
       "manager":True
       },
       {
       "name":"Jenny",
       "salary":50000,
       "manager":False
       },
       {
       "name":"Tony",
       "salary":40000,
       "manager":False
       }
   ]
})
print("---------------------------")

# 要求三
def func(a):
   def mutiply(x, y):
       print(a+(x*y))
   return mutiply
 
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
print("---------------------------")
 
	
# 要求四
# 方法一
# def maxProduct(nums):
#    if len(nums) == 2:
#        return nums[0] * nums[1]
  
#    negative = []
#    positive = []
#    for i in nums:
#        if i < 0:
#            negative.append(i)
#        else:
#            positive.append(i)      
 
#    value1 =0
#    value2 =0
#    if len(negative) >= 2 :
#        neg1 = min(negative)
#        negative.remove(neg1)
#        neg2 = min(negative)
#        value1 = neg1 * neg2
#    if len(positive) >= 2 :
#        pos1 = max(positive)
#        positive.remove(pos1)
#        pos2 = max(positive)
#        value2 = pos1 * pos2
#    if value1 > value2:
#        return value1
#    else:
#        return value2

# 方法二
def maxProduct(nums):
    max_num = nums[0]
    min_num = nums[0]
    ans = nums[0] * nums[1]
    for i in range(1, len(nums)):
        ans = max(max_num * nums[i], min_num * nums[i], ans)
        max_num = max(max_num, nums[i])
        min_num = min(min_num, nums[i])
    print(ans)   


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10
print("---------------------------")
 
# 要求五
def twoSum(nums, target):
   for i in range(len(nums)):
       for n in range(i+1, len(nums)):
           if nums[i] + nums[n] == target:
               return [i, n]
 
result=twoSum([2, 11, 7, 15], 9)
print(result)
print("---------------------------")
 
# 要求六
# 方法一
# def maxZeros(nums):
#    zero =[]
#    count = 0
#    for i in nums:
#        if i == 0:
#            count +=1
#            zero.append(count)
#        else:
#            count = 0
#    if len(zero) == 0:
#        print(0)
#    else:
#        print(max(zero))
 
# 方法二
def maxZeros(nums):
    max_len = 0
    count = 0
    for i in nums:
        if i == 0:
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0
    print(max_len)
 
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
