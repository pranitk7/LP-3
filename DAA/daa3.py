class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def fractionalknapSack(W, arr):
    
    arr.sort(key= lambda x: (x.profit/x.weight), reverse=True)
    res = 0.0

    for item in arr:

        if item.weight <= W:
            W = W - item.weight
            res = res + item.profit
        else:
            res = res + item.profit*W/item.weight
            break
    
    return res




if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    print(fractionalknapSack(W, arr))
