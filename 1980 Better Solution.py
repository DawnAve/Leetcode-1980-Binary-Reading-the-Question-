class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        for i in range(pow(2,n)):
            t=bin(i).replace('0b','')
            if len(t)<n:
                s='0'*(n-len(t))
                t=s+t
            if t not in nums:
                return t
