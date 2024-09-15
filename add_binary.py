class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary_value1 = int(a , 2)
        binary_value2 = int(b , 2)

        result_value = binary_value1 + binary_value2

        binary_value = bin(result_value)[2:]
        string_value = str(binary_value)
        
        return string_value


sol = Solution()
print(sol.addBinary("11","1"))