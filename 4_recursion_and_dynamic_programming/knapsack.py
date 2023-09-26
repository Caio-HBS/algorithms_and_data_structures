"""
You're in charge of selecting a football team from a large pool of players. Each 
player has a cost and a rating. You have limited budget. What is the highest total 
rating of a team that fits your budget? Assume that there's no minimum or maximum 
team size.
"""

from colorama import Style, Fore

from test_cases_knapsack import test_list, test_print


# Recursive approach.
def max_profit_recursive(
    weights: list, profits: list, capacity: int, idx: int = 0
) -> int:
    """
    Takes in two lists with the weights and profits for each element and uses
    recursion to determine what are the best elements for that capacity. Returns
    the maximum profit for a given capacity.

    Args:
        weights: a list with the weights of each element;
        profits: a list with the profits of each element;
        capacity: the total capacity for the team;
        idx: index for recursion. Defaults to 0.
    """

    # We have reached the end of the list.
    if idx == len(weights):
        return 0

    # Ignore that number because we can't fit it into the capacity.
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx=(idx + 1))

    # Boils down to two options, we simply take the max because it's the optimal
    # solution.
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx=(idx + 1))
        option2 = profits[idx] + max_profit_recursive(
            weights, profits, capacity=(capacity - weights[idx]), idx=(idx + 1)
        )
        return max(option1, option2)


#Dynamic programming approach.
def max_profit_dynamic(weights: list, profits: list, capacity: int) -> int:
    """
    Takes in two lists with the weights and profits for each element and uses
    recursion to determine what are the best elements for that capacity. Returns
    the maximum profit for a given capacity.

    Args:
        weights: a list with the weights of each element;
        profits: a list with the profits of each element;
        capacity: the total capacity for the team.
    """
    
    #
    n = len(weights)
    table = [ [0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n):
        for c in range(1, (capacity + 1)):
            if weights[i] > c:
                table[(i + 1)][c] = table[i][c]

            else:
                table[(i + 1)][c] = max(table[i][c], profits[i] + table[i][(c - weights[i])])

    return table[-1][-1]


# Print the tests
print(
    "\nMAX PROFIT TESTS" + Fore.CYAN + " (RECURSION):\n",
    Style.RESET_ALL,
)
test_print(test_list, max_profit_recursive)

print(
    "\nMAX PROFIT TESTS" + Fore.CYAN + " (DYNAMIC):\n",
    Style.RESET_ALL,
)
test_print(test_list, max_profit_dynamic)
