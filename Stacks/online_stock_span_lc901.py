# Online Stock Span
# Leetcode 901
# https://leetcode.com/problems/online-stock-span/

class StockSpanner:
    """Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

    The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

    For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days.
    Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

    Time complexity: Amortized O(1) / O(n) [worst]
    Space complexity: O(n)
    """
    def __init__(self):
        self.prices: list[(int, int)] = [] # stack
        self.prev_span: int = 0 # last span seen
        self.prev_price: int = 0 # last price seen
        self.n: int = 0 # how many prices we have seen total

    def next(self, price: int) -> int:
        self.n += 1

        if price < self.prev_price:
            self.prev_span = 1
        elif price == self.prev_price:
            self.prev_span += 1
        else:
            while len(self.prices) > 0 and price >= self.prices[-1][0]:
                self.prices.pop()
            
            if len(self.prices) == 0:
                self.prev_span = 1
            else:
                self.prev_span = self.n - self.prices[-1][1]

        self.prices.append((price, self.n))
        self.prev_price = price

        return self.prev_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)