li=[11,22,33,44]
def f1(arg):
    arg.append(55)

li=f1(1)
f1(li)
print(li)
