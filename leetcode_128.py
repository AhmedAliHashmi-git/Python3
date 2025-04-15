class Solution:
    def longestConsecutive(self, nums):
        s = set(nums) 
        L = sorted(s)  
        L2 = []
        L3 = []

        for i in range(len(L)):
            if i == 0 or L[i] == L[i - 1] + 1:
                L3.append(L[i])
            else:
                if len(L3) > len(L2):
                    L2 = L3
                L3 = [L[i]]  

        if len(L3) > len(L2):
            L2 = L3.copy()  

        return len(L2)

    


if __name__ == "__main__":
    nums = list(map(int, input("Enter the list of numbers: ").split()))
    sol = Solution()
    print(sol.longestConsecutive(nums))
