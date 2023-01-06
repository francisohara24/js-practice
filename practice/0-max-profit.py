# Sample Programming Interview Question from interviewcake.com


# First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.
#
# So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:
#
# The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
# The values are the price (in US dollars) of one share of Apple stock at that time.
# So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.
#
# Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
#


def get_max_profit(stock_prices: list) -> float:
    max_profit = float("-inf")

    for i in range(len(stock_prices) - 1):
        for j in range(i + 1, len(stock_prices)):
            profit = stock_prices[j] - stock_prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


stock_prices = [1, 2, 3, 4, 5, 15]
print(get_max_profit(stock_prices))
