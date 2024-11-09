"""
Problem Name: Encrypted Message

A pack of hyenas has created their own little code so they can communicate secretly. One tells give you a message and it is your job to decode it.

His message corresponds to the following instruction set with the following commands:

“>”: move the pointer one cell to the right
“<”: Move the pointer one cell to the left
“+”: Increment the value at the current cell by 1.
“-”: Decrement the value at the current cell by 1.
“.”: Output the ASCII character represented by the value at the current cell
The memory comprises an array of 10 cells initialized at zero wherein the pointer begins at the first cell.

The instructions correspond to their ascii values as do the outputs given by the “.” instruction

**Input Format**

N, the number of instructions Next N line contains two values separated by a colon

The base of the instruction (an integer between 2 and 16).
The encoded instruction in that base
Constraints

N will always be less than 500.

The base will always be between 2 and 16, inclusive.

**Output Format**

Only output what is specified by the “.” instruction.

**Sample Input 0**
34
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101011
2:101110

**Sample Output 0**
!

**Explanation 0**
Cell 0 is incremented 33 times and then displayed
"""

arr = [0] * 10
p = 0
n = int(input())

for x in range(n):
    b, i = input().split(":")
    i = chr(int(i, int(b)))
    if i == ">":
        p += 1
    elif i == "<":
        p -= 1
    elif i == "+":
        arr[p] = (arr[p] + 1) % 256
    elif i == "-":
        arr[p] = (arr[p] - 1) % 256
    elif i == ".":
        print(chr(arr[p]), end="")