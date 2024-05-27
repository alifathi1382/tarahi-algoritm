from numpy import array

a = array([
    [1, 2, 3],
    [4, 5, 6]
])

d = array([
    [6, 5, 4],
    [3, 2, 1]])

b = array([
    [6, 5, 4],
    [3, 2, 1],
    [7, 8, 9]
])

print(a)
print(b)
c = a.dot(b)
f = a * d
e = a + d
h = a - d
g = a / d
print(c)
print(g)
print(g.dtype)
print(f)
print(e)
print(h)
