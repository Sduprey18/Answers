class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if nums.count == 0 || nums.count == 1{
          return nums.count
        }
        
        var l = 0
        var r = 1
        while r<nums.count{
          if nums[l] == nums[r]{
            nums.remove(at: r)
          } else{
            l+=1
            r+=1
          }
        }
        return nums.count
    }
}