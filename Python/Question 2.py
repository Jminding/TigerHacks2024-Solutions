"""
Problem Name: String Swap

Given a string, s, of length L and n rules containing i and j: switch the character in position i with the character in position j. The first character is in position 0 not position 1.

**Input Format**

The first line of the input contains L and n space separated

The second line of the input contains the string s

The next n lines of the input contain i and j space separated

**Constraints**

L and n will not be greater than 100

i and j will not be greater than L - 1

s will be made up of only uppercase and lowercase letters

**Output Format**

Output the scrambled string

**Sample Input 0**
5 2
Tiger
2 3
0 3

**Sample Output 0**
gieTr

**Explanation 0**

For the first rule, we switch the characters in positions 2 and 3. In this case, we are switching the “g” and “e” which yields “Tiegr”.

For the second rule, we switch the character in positions 0 and 3. Here we switch the “T” and “g” which yield “gieTr.”

We have now completed all the rules so we output “gieTr.”
"""

L, n = map(int, input().split())
s = list(input())

for x in range(n):
    i, j = map(int, input().split())
    temp = s[i]
    s[i] = s[j]
    s[j] = temp

print("".join(s))