# Best Time to Buy and Sell Stock
# Leetcode 121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def best_time_to_buy_and_sell_stock_lc121(prices: list[int]) -> int:
    """You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Time complexity: O(n)
    Space complexity: O(1)

    :param prices: The list of prices, with index corresponding to price on ith day
    :type prices: list[int]

    :rtype: int
    :return: Maximum profit which can be made
    """
    max_seen_profit: int = 0 # 'If you cannot achieve any profit, return 0.'

    buying_day: int = 0

    for selling_day in range(1, len(prices)):
        # find lowest buying cost and remember this day
        if prices[selling_day] < prices[buying_day]:
            buying_day = selling_day

        profit: int = prices[selling_day] - prices[buying_day]

        max_seen_profit = max(profit, max_seen_profit)
    
    return max_seen_profit