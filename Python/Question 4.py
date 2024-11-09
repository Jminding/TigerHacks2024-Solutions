"""
Problem Name: Mischievous Monkeys

Safarist Robert is in shambles in many respects, as the safari animals do not respect his authority and frequently mess around with him. The latest pranks the Monkeys have played on him was to steal his meticulous zookeeping notes and scramble everything. To do this, they simply shifted all the letters a certain number of times to the right (i.e., to shift ‘A’ twice to the right would yield ‘C’). Spaces should remain spaces. The number of times they shifted is given by the ASCII value (a numerical value that represents letters) of the last letter of the final word of the fifth sentence in the rules. Your job is to help Zookeeper Robert by un-encrypting his important files. We guarantee all characters in the unscrambled message are capital letters or spaces, and that each sting is less than 500 characters long.

**Input Format**

The scrambled string

**Constraints**

All characters in the unscrambled message are capital letters or spaces, and that each sting is less than 500 characters long

**Output Format**

The unscrambled string

**Sample Input 0**
QFFBU

**Sample Output 0**
APPLE
"""

s = list(input())
shift = 16
ret = ""
for i in s:
    if i == " ":
        ret += " "
        continue
    ret += chr((ord(i) - (shift - 65)) % 26 + 65)

print(ret)