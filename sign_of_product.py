class Solution:
    def arraySign(self, nums: list[int]) -> int:
        count =0 
        if 0 in nums:
            return 0
        for i in nums:
            if i<0:
                count +=1
        
        if count%2==0:
            return 1
        else:
            return -1

n =[]
l=int(input("Enter size : "))
print("Enter desired input : ")
for i in range(0,l):
    ele = int(input())
    n.append(ele)
print("*****************************************")
print(f"Entered Array is = {n}")
print("*****************************************")
print()
num= Solution()
print("*****************************************")
print(f"Sign of Product of required array is = {num.arraySign(n)}")
print("*****************************************")