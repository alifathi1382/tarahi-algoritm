from numpy import array, empty, zeros, ones
from numpy.linalg import norm

l1 = [1, 2, 3, 4]
print(l1)
a = array(l1)
print(a)
print(a.shape)
print(a.dtype)
b = empty([3, 3])
print(b)
c = zeros([5, 2, 2])
print(c)
d = ones([2, 2])
print(d)
data = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]

])
split = 2
tr, tes = data[:split, :], data[split:, :]
print(tr)
# print(tes)
mm = array([3, 2, 1])
gg = array([6, 5, 4])
j = mm.dot(gg)
print(j)
t = mm @ gg
print(t)
f = array([1, -2])
l1 = norm(f, 3)
