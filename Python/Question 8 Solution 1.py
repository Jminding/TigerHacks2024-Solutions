"""
Problem Name: Predicting States

Imagine a vast safari where every animal herd can be in one of two states: state A or state B. As the herds roam across the plains, they may shift between states based on certain probabilities, creating dynamic patterns that shift like the movement of the great migration. Your task is to track these transitions and determine the stable distribution of herds between the states — a challenge that requires keen observation and sharp analytical skills. So grab your binoculars and prepare to uncover the hidden order of the savanna's wandering wildlife!

You are given a table of probabilities:

                        Ending in state A   Ending in state B
Starting in state A     0.6                 0.4
Starting in state B     0.7                 0.3

The table indicates the probability of a given end state, A or B, given a specific starting state, A or B.

For example, if the starting state is A, the probability of ending in state A is 0.6 or 60% and the probability of ending in state B is 0.4 or 40%. Over time, as states A and B transition, there emerges a general distribution of the probability of states A and B, one that does not necessarily depend on the prior state.

There is a way to find the general probabilities of each state that involves plugging in any starting state. Consider, for example, we start in state A, where the probability of remaining in A = 0.6 and going to B = 0.4, then for the next iteration, irrespective of the state we land in:

P(A) = 0.64 P(B) = 0.36

Note that this distribution is not a weighted average. In this case, the general probability of state A converges to 0.63 repeating and state B to 0.36 repeating.

From this table you can find the probability of each event regardless of the starting state.

And output them, space separated, rounded to 6 decimal places. Hint: P(A) + P(B) = 1

**Input Format**

The 4 lines of input contain top left, top right, bottom left, and bottom right values of the table in that order.

**Constraints**

The given inputs will not have more than 4 digits after the zero. The given inputs will always be between one and zero, never one or zero

**Output Format**

The output should be P(A) and P(B), space-separated. This output should include the decimal point and the leading zero. This output will always be between 1 and 0.

**Sample Input 0**
0.6
0.4
0.7
0.3

**Sample Output 0**
0.636364 0.363636
"""

a = float(input())
b = float(input())
c = float(input())
d = float(input())

x = c / (1 - a + c)
y = 1 - (c / (1 - a + c))

print(f"{round(x, 6)} {round(y, 6)}")

"""
Reasoning:
The table of probabilities forms a Markov Chain, which can be solved with the following system:
         | a  b |   | x |
| x  y | |      | = |   |
         | c  d |   | y |

Where a, b, c, and d are the probabilities given in the input, and x and y are the probabilities of being in state A and B, respectively. Therefore, the solution to this system can be found by solving the following equations:

ax + cy = x
cx + dy = y
x + y = 1 (as stated in the problem since this is about probabilities)

Interestingly, a normal transition matrix would be represented as the transpose of the matrix shown above, which would result in a normal eigenvector equation.

The result of solving for x and y are shown above.
"""