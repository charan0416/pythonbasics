l = ["porcshe","bmw","merc","bentley"]
l1 = [x if x!="bmw" else "mustang"for x in l]
print(l1)
#sugs
l2=[y for y in l]
print(l2)
#hdhs
l3=[x for x in l1 if x!="porcshe"]
print(l3)
#esggs
l4 = [x for x in l1 if x=="bentley"]
print(l4)
#upper
l5 = [x.upper() for x in l1]
print(l5)
l6=[x.lower() for x in l1]
print(l6)
#dict
names = ['John', 'Alice', 'Bob', 'Lucy','charan']
scores = [85, 90, 78, 92,22,43]

res = (zip(names, scores))
print(dict(res))