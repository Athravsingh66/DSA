# Question

# Leetcode 121 - Best Time to Buy and Sell Stock


# Solution


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit



# Another Way to slove but it will take more time and in competitive time limit exceed



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        r=[0]
        for i in range(len(prices)):
            a=prices[i]
            for j in range(i+1,len(prices)):
                b=prices[j]-a
                r.append(b)
                
        return max[r]
            