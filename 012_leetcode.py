"""leetcode 70

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

# # FIBONACCIrecursive 
# #递归的问题，容易超时间
# class Solution:
#     def climbStairs(self, n):
#         if n<1: return 0
#         if n==1: return 1
#         if n==2: return 2
#         return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution:
    def climbStairs(self,n:int)->int:
        if n<1:return 0
        if n==1:return 1
        if n==2:return 2
        
        if n > 2:
            all_step=[]
            all_step.append(1)
            all_step.append(2)
            for i in range(2,n):
                all_step.append(all_step[i-2] + all_step[i-1])
            return all_step[-1]
                


"""Leetcode 69
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

#遍历 递归 太慢了...
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x==0: return 0
#         if x==1: return 1
        
#         for i in range(int(x/2)+1):
#             cur = i*i
   
#             if cur == x: return i
#             if cur > x: return i-1
#             else:
#                 if (

# well this is simple, but still too slow
# class Solution:
#     def mySqrt(self,x:int)->int:
#         for i in range(x+2):
#             if i*i>x:
#                 break
#         return i-1


        

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        lo, hi = 0, x
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid ** 2 > x:
                hi = mid
            else:
                lo = mid + 1
        
        return hi - 1

"""Leetcode 83
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#use slow fast pointer to enumerate the list  #python如何创建新的空 Listnow .  a = ListNode(0)
#Head: ListNode 为了声明参数格式 :ListNode, ->ListNode表示返回类型
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        slow =head       
        if(slow == None): return None
        fast = slow.next
        while(fast != None):
            if(fast.val != slow.val):
                slow.next = fast
                slow = slow.next
                fast = fast.next
               
            else: fast = fast.next
        slow.next = None
        return head
        
"""Leetcode 88
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""

        
        
class Solution:
  
    def merge(self, nums1, m, nums2, n):
        L = nums1[:m] + nums2
        L.sort()
        i = 0
        while i < len(L):
            nums1[i] = L[i]
            i+=1



        
        


    
    
  
