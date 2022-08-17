# You are visited a farm to collect fruits. The farm has a single row of fruit trees.
# You will be given two baskets, your goal is to pick as many fruits as possible to be placed
# in the given baskets.
#
# You will be given an array of characters where each character represents a fruit tree.
# The farm has the following restrictions:
#
#   1. Each basket can have only one type of fruit.
#      There is no limit to how many fruit a basket can hold.
#   2. You can start with any tree, but you can't skip a tree once you have started
#   3. You will pick exactly one fruit from every tree until you cannot, i.e., you will
#      stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both baskets.
#
# Example:
#   Input: Fruit=['A', 'B', 'C', 'A', 'C']
#   Output: 3
#   Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray
#                ['C', 'A', 'C']

def fruits_into_basket(fruit):
    start = 0
    baskets = {}
    max_fr00t = 0

    for end in range(len(fruit)):
        if fruit[end] not in baskets:
            baskets[fruit[end]] = 1
        else:
            baskets[fruit[end]] += 1

        while len(baskets) > 2:
            baskets[fruit[start]] -= 1
            if baskets[fruit[start]] == 0:
                del baskets[fruit[start]]
            start += 1

        max_fr00t = max(max_fr00t, end-start+1)

    return max_fr00t


fruits_into_basket(['A', 'B', 'C', 'A', 'C'])