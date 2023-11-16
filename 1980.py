class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        baseTen = []
        for i in nums:
            baseTen.append(int(i,2))
        if baseTen[0] != 0:
            return '0'*len(nums[0])
        for i in range(len(baseTen)-1):
            if baseTen[i] +1 < baseTen[i+1]:
                binary = str(bin(baseTen[i]+1))
                binary = binary[2:]
                if len(binary)<len(nums[0]):
                    binary = '0'*(len(nums[0])-len(binary))+binary
                
                return binary
        length = 2**len(nums[0])
        if len(baseTen) < length:
            binary = bin(length-1)
            return binary[2:]
                
                    
