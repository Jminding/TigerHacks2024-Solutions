"""
Problem Name: Pangolin Polynomials (should have "Pangolin Polygons")

The pangolins on our safari love to perform artistic displays by orienting themselves into shapes along the savannah (do pangolins live in the Savannah? Questions for Zookeeper Robert...) In any case, the Safari administration wants to determine the area of the shapes made by the pangolins, in order to use it for promotional activities. The polygons that the pangolins form are simple, i.e. they do not intersect themselves.

**Input Format**

The first line of input is n, the number of pangolins.

The next n lines each contain x and y, the coordinate of the i-th pangolin.

**Constraints**

We guarantee that the polynomial is a planar, simple polygon, and that the points are all oriented correctly, i.e., they appear in order, counter clockwise. We guarantee that n < 1000. Furthermore, we guarantee that all coordinate points (x,y) are integer values less than 100,000,000.

**Output Format**

Return the UNSIGNED area of the polygon that the pangolins form, rounded to the nearest whole number (round up for .5).

**Sample Input 0**
4
1 4
3 6
4 4
2 1

**Sample Output 0**
8
"""

n = int(input())
x = []
y = []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    
area = 0
for i in range(n):
    j = (i + 1) % n
    area += (x[i] * y[j] - x[j] * y[i])

area = abs(area)/2
if n == 2:
    area = 0
print(int(area + 0.5))