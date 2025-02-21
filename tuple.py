t = ("charan",25,'mahabubnagar')
print(type(t))
t2 =("sriya",'26','nagole')
t3 = t + t2
print(t3)
print(t[0])
t4=list(t3)
t4.remove("charan")
print(t4)
print(t3)

print(t4)
print(t3)
print(t3[0:3])
print(t3[2:])
print(t3[:4])
if "charan" in t3 :
    print("true")
else:
     print("false")
