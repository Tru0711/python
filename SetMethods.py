print(" SET METHODS IN PYTHON")
print("***************************************************")
s = {1,2,3,2,3,2,2,4,5,6,7,8,9,10}
print(s)
s1 = s.add(11)
print("add() : \n", s)
print("--------------------------------------------------")
s2 = s.clear()
print("clear() : \n", s)
print("--------------------------------------------------")
set1 = {"shreya","shrujana","srujana"}
s3 = set1.copy()
print("copy() : \n", set1)
print("--------------------------------------------------")
S1 = {'vedu','rahi','riya','kajal','reva','niva'}
S2 = {'raj','vedu','nick','noha','isha','kajal','reva'}
print(S1)
print(S2)
# x = S1.difference(S2)
x = S1 - S2
print("Difference() : \n", x)
print("--------------------------------------------------")
S1.difference_update(S2)
# S1 -= S2
print("Difference update() : \n", S1)
print("--------------------------------------------------")
print(set1)
set1.discard("shreya")
print("discard() : \n", set1)
print("--------------------------------------------------")
x1 = {1,2,3,4,5,6,7,4,3,2,8,9,0}
x2 = {2,3,7,3,8,91,10,21}
print(x1)
print(x2)
x1 = x1.intersection(x2)
# x1 & x2
print("intersection() : \n", x1)
print("--------------------------------------------------")
p1 = {21,12,34,21,87,99,43}
p2 = {43,65,9,32,49,99,21,40,20,6,7,32}
print(p1)
print(p2)
#p1.intersection_update(p2)
p1 &= p2
print("Insertion update() : \n", p1)
print("--------------------------------------------------")
print(p1)
print(p2)
print("isdisjoint() : \n", p1.isdisjoint(p2))
print("--------------------------------------------------")
print(p1)
print(p2)
print("issubset() : \n", p1.issubset(p2))
print("--------------------------------------------------")
print(p2)
print(p1)
print("isupperset() : \n", p2.issuperset(p1))
print("--------------------------------------------------")
print(p1)
print("pop() : \n", p1.pop())
print("After pop : \n", p1)
print("--------------------------------------------------")
print(p2)
p2.remove(49)
print("remove() : \n", p2)
print("--------------------------------------------------")
print(p2)
print(p1)
P = p2.symmetric_difference(p1)
print("symmetric_difference() : \n", P)
print("--------------------------------------------------")
print(p1)
print(p2)
p1.symmetric_difference_update(p2)
print("symmetric_diff_update() : \n", p1 )
print("--------------------------------------------------")
m = {"Shreya","Riya","Kartik","Diya","Roh","Radha"}
n = {"Raj","Mahish","Nick","Noha","Riya","Roh"}
print(m)
print(n)
print("union() : \n", m.union(n))
print("--------------------------------------------------")
print(m)
print(n)
print(p1)
m.update(n,p1)
print("update() : \n", m )
print("***********************-----------------------------*******---------------------*******************")










