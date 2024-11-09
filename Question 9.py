"""
Problem Name: Compound Words

Given a target compound word t, and n number of words, w_0, w_1, w_2, …, find the two words that make up the compound word and return the two indexes of the words that make up the compound word in increasing order.

**Input Format**

The first line of the input contains t

The second line of the input contains n

The next n lines of the input contain the w's

**Constraints**

It is guaranteed that the target compound word, t, will always be less than 500 characters

It is guaranteed that each word, w, will always be less than 250 characters

It is guaranteed that n will be less than 10^6

It is guaranteed that each w will be unique

**Output Format**

The output should contain the two indexes space separated

**Sample Input 0**
wildlife
3
lion
life
wild

**Sample Output 0**
1 2

**Explanation 0**
The two words that make up “wildlife” are “wild” and “life”

“wild” appears first and has an index of 2

“life” appears second and has an index of 1

The output is 1 2 because 1 is less than 2
"""

t = input()
n = int(input())
words = []
for i in range(n):
    words.append(input())

ret = []

for i in range(n):
    if words[i] in t:
        ret.append(i)

print(" ".join(list(map(str, sorted(ret)))))