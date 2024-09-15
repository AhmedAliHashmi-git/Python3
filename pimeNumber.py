# class Solution:
#     def primeNumber(self , n:int)->None:
#         count = 0
#         for i in range(1 , n+1):
#             if n % i == 0:
#                 count = count + 1
#         if count > 2:
#             print("Not a prime Number")
#         else:
#             print("Prime Number")


# sol = Solution()
# sol.primeNumber(20)


class Solution:
    def primeNumber(self , a: int , b: int)->None:
        count = 0
        list = []
        for i in range(a , b+1):
            count = 0
            for j in range(1 , b+1):
                if i % j == 0:
                    count = count + 1
            if count == 2:
                list.append(i) 
        print(list)


sol = Solution()
sol.primeNumber(16 , 33)