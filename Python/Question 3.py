"""
Problem Name: Binary Search Tree

Given n numbers of nodes, k_0 to k_n-1, where each k is an integer: construct a binary search tree with the nodes and output the sum of the values of the nodes with no children. Each node should be inserted into the tree in the given order. The tree should not be automatically balanced or altered after a node is inserted.

**Input Format**

The first line of input is n followed by n lines of k values

**Constraints**

It is guaranteed that n is less than 10^3

It is guaranteed that all k's will be positive integers less than 10^3

**Output Format**

The output should be a single integer

**Sample Input 0**
4
20
10
30
15

**Sample Output 0**
45

**Explanation 0**
Explanation is on the paper problem set or the pdf
"""

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n = int(input()) - 1

root = node(int(input()))

for i in range(n):
    data = int(input())
    current = root
    while True:
        if data <= current.data:
            if current.left is None:
                current.left = node(data)
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = node(data)
                break
            else:
                current = current.right

def count_no_children(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    return count_no_children(root.left) + count_no_children(root.right)

print(count_no_children(root))
