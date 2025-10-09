class Solution:
    def maxProfit(self, prices):
        """
        Calculates the maximum profit from a single stock transaction.

        Args:
            prices (list[int]): A list of stock prices on consecutive days.

        Returns:
            int: The maximum possible profit.
        """
        # `min_price` keeps track of the lowest price encountered so far.
        # It's initialized to positive infinity to ensure the first price
        # in the list will be the initial minimum.
        min_price = float('inf')
        
        # `max_profit` stores the maximum profit found up to the current day.
        # It's initialized to 0, as profit cannot be negative.
        max_profit = 0
        
        # We iterate through each `price` in the list of stock prices.
        for price in prices:
            # If the current price is less than the `min_price` we've seen,
            # we update `min_price` to this new, lower value. This is our
            # best possible day to buy so far.
            if price < min_price:
                min_price = price
            # If the current price is not a new minimum, we check if selling at this price
            # would yield a better profit than our current `max_profit`.
            # The potential profit is `price - min_price`.
            elif price - min_price > max_profit:
                # If the new potential profit is greater, we update `max_profit`.
                max_profit = price - min_price
                
        # After checking all prices, `max_profit` holds the highest profit
        # that could have been made.
        return max_profit
