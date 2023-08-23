from typing import List

def knapsack_weight_only(weights: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    result = []
    memo = [[False for _ in range(13)] for _ in range(len(weights) + 1)]
    def dfs(val, start_index, memo):
       if memo[start_index][val]:
          return
       if start_index == len(weights):
          result.append(val)
          return
       #result.add(val)
       dfs(val + weights[start_index], start_index + 1, memo)
       dfs(val, start_index + 1, memo)
       memo[start_index][val] = True
       return result
    
    return dfs(0, 0, memo)

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    res = knapsack_weight_only(weights)
    #res.sort()
    for i in range(len(res)):
      print(res[i], end='')
      if i != len(res) - 1:
        print(' ', end='')
    print()
