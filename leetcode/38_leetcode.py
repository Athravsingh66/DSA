# Question
# LeetCode 38 - Count and Say


# Solution
class Solution:
    def countAndSay(self, n: int) -> str:  
        if n == 1:
            return "1"
        
        a = "1"
        
        for _ in range(n-1):
            result = []
            i = 0
            
            while i < len(a):
                count = 1
                
                while i+1 < len(a) and a[i] == a[i+1]:
                    count += 1
                    i += 1
                    
                result.append(str(count))
                result.append(a[i])
                
                i += 1
                
            a = "".join(result)
            
        return a
    
            