from typing import List
from math import inf

def dfs(sum_t, coins, amount, memo):
    if sum_t == amount:
        return 0
    if sum_t > amount:
        return inf
    if (memo[sum_t] != -1):
        return memo[sum_t]
    
    ans = inf
    for coin in coins:
        result = dfs(sum_t + coin, coins, amount, memo)
        if result is inf:
            print("skipped sum: %d for coin %d" %(sum_t, coin))
            continue
        ans = min(result + 1, ans)
        print("ans for sum : %d is %d at coin %d" %(sum_t, ans, coin))
    memo[sum_t] = ans
    return ans

def coin_change(coins: List[int], amount: int) -> int:
    # WRITE YOUR BRILLIANT CODE HER
    memo = [-1] * (amount + 1)
    result = dfs(0, coins, amount, memo)
    
    return -1 if result == inf else result

if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
