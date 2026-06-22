"""
Author: Jennifer
Date: June 21, 2026
File Name: lemonadeStand.py
Description: This program simulates a lemonade stand. It uses functions to
calculate the total cost of ingredients and the profit from sales.
"""

# Defining a function to calculate the total cost of lemonade ingredients
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost # Adding ingredient costs together
    return total_cost # Returning the calculated total cost

# Defining a function to calculate the profit from selling the lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost) # Calling our cost function
    profit = selling_price - total_cost # Subtracting cost from selling price
    return profit # Returning the calculated profit

# Creating variables to test each function
cost_of_lemons = 5.00
cost_of_sugar = 3.00
price_to_sell = 15.00

# Calling the functions and storing the mathematical results
calculated_cost = calculate_cost(cost_of_lemons, cost_of_sugar)
calculated_profit = calculate_profit(cost_of_lemons, cost_of_sugar, price_to_sell)

# Building output strings using an output variable and string concatenation
cost_result = str(cost_of_lemons) + " + " + str(cost_of_sugar) + " = " + str(calculated_cost)
profit_result = "Total Profit: " + str(calculated_profit)

# Printing the results to the console
print(cost_result)
print(profit_result)