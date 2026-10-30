
prices = [7, 2, 1, 5, 5, 7, 0,-7]
def find_best_time(prices):
    min=None
    max_profit=0
    indexing=[]
    for i in range(len(prices)):
        if min is None:
            min=prices[i]
            continue
        if prices[i]<min:
            min=prices[i]
            continue
        calc_profit=prices[i]-min
        if calc_profit>max_profit:
            indexing.clear()
            indexing.extend([min,prices[i]])
            max_profit=calc_profit
    return indexing,max_profit
print(find_best_time(prices))