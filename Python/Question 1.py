"""
Problem Name: Pricing Tickets

A group wants to purchase tickets for a safari. An adult ticket costs 10 dollars and a child ticket costs 5 dollars. Given n adults and m children, find the total cost for the group to purchase tickets for everybody.

**Input Format**

The first line of input will contain n

The second line of input will contain m

**Constraints**

It is guaranteed that n and m will not be greater than 10^4

**Output Format**

The output should be a single integer

**Sample Input 0**
3
4

**Sample Output 0**
50
"""

n = int(input())
m = int(input())
print(n * 10 + m * 5)