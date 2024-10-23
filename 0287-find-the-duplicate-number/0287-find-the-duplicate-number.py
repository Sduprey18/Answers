class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyd cycle detection
        slow, fast = nums[0], nums[0]
        #treat this as a ll, since you know that theyre numbered 1 to n
        #use the values to tell u what "node" to go to next
        while True:
            #move fast pointer 2 steps
            fast = nums[nums[fast]]
            #then you move the slow pointer only one
            slow = nums[slow]
            '''
            you found the cycle, and there is NO chance of fast going out of bounds, because
            this question is guarnateeed to give u a cycle, since the numbers are from 1-n,
            with the arr size being n+1
            '''
            if slow == fast:
                break
        
        #ok, since you found the cycle, you restart again, put one of the pointers to 0 
        #(doesnt matter which one, then return either pointer)

        slow = nums[0]
        while slow!= fast:
            fast = nums[fast]
            slow = nums[slow] 
        return slow

