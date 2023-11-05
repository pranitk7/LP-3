

def knapSack(W, wt, val, n):

    if n == 0 or W == 0:
        return 0
    
    if t[n][W] != -1:
        return t[n][W]
    
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1]+knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapSack(W, wt, val, n-1)
        return t[n][W]

    



if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    t = [[-1 for i in range(W+1)] for j in range(n+1)]
    print(knapSack(W, weight, profit, n))