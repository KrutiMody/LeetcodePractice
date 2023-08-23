from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    result = []
    def dfs(node, path):
        #if all (c is None for c in node.children):
        if not node.children:
            #result.append('->'.join(path) + '->' + str(node.val))
            path.append(node.val)
            result.append(path[:])
            #print(result)
            return
        path.append(node.val)
        #print(path)
        for child in node.children:
            dfs(child, path)
            path.pop()
    if root:
        dfs(root, [])
    return result

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
