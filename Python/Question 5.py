"""
Problem Name: Giraffe Problem

Somewhere in the wilderness, a giraffe exists. They have given you a 5x5xn 3D array wherein n represents the number of layers. The goal is to identify the treasure location on the grid based on the values in the grid based on the values within each cell. The grid is initially incomplete, with some cells represented by a “?”.

Find the formula to calculate the missing values in the Commons. (Since the problem has already been solved: the formula is i + j + 2k + 1.)

After completing the grid, find the layer and the coordinates (i, j) where the sum of the row values is the highest across all layers and rows. This row with the highest sum reveals the treasure’s location.

There is a specific formula you need to calculate the unknown values. To figure out the formula, search the large room where we all first met (yes you actually have to get up and go).

Where i and j are row and column indices and k is the layer index (all 0-indexed)

After filling in the cells identify the row with the maximum sum

Return the layer and row (“k i”) where this row exists

**Input Format**

First Line: n, number of layers

Next n blocks: each layer is a 5x5 grid, with rows represented by a space separated numbers or “?” for unknowns

**Constraints**

n will not be greater than 500

**Output Format**

k and i space separated
"""

n = int(input())
arr = []

for i in range(n):
    layer = []
    for j in range(5):
        layer.append(input().split(" "))
    arr.append(layer)
for k in range(n):
    for i in range(5):
        for j in range(5):
            if arr[k][i][j] == "?":
                arr[k][i][j] = i + j + 2 * k + 1
            else:
                arr[k][i][j] = int(arr[k][i][j])

max_k, max_i = 0, 0
max_sum = 0
for k in range(n):
    for i in range(5):
        curr_sum = sum(arr[k][i])
        if curr_sum > max_sum:
            max_k, max_i = k, i
            max_sum = curr_sum

print(max_k, max_i)
