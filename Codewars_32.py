#Find the maximum single sell profit
#You are provided with the list of stock prices, and you have to return the buy and sell price to make the highest profit. 
#Note: We have to make maximum profit from a single buy/sell, and if we can’t make a profit, we have to reduce our losses. 
#Example 1: stock_price = [8, 4, 12, 9, 20, 1], buy = 4, and sell = 20. Maximizing the profit. 
#Example 2: stock_price = [8, 6, 5, 4, 3, 2, 1], buy = 6, and sell = 5. Minimizing the loss.

def buy_sell_stock_prices(stock_prices):
    current_buy = stock_prices[0]
    global_sell = stock_prices[1]
    global_profit = global_sell - current_buy

    for i in range(1, len(stock_prices)):
        current_profit = stock_prices[i] - current_buy

        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = stock_prices[i]

        if current_buy > stock_prices[i]:
            current_buy = stock_prices[i]

    return global_sell - global_profit, global_sell

stock_prices_1 = [10,9,16,17,19,23]
buy_sell_stock_prices(stock_prices_1)
# (9, 23)


stock_prices_2 = [8, 6, 5, 4, 3, 2, 1]
buy_sell_stock_prices(stock_prices_2)
# (6, 5)

#another way of solving this.

a = [8, 4, 12, 9, 20, 1]

[j for i in (list(filter(lambda n: len(n) >=2,i)) for i in ([[a[i:i+2] for 
                            i in range(len(a)-(3-1))]+[a[i::3]for i in range(len(a))]+[a[i::4]for i in range(len(a))]])) for j in i]
[[8, 4], [4, 12], [12, 9], [9, 20], [8, 9], [4, 20], [12, 1], [8, 20], [4, 1]]
    