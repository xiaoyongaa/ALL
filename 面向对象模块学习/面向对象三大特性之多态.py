#多种类型
面向对象的三大特性
3.多态（多种形态，多种类型）
def func(arg):
    print(arg)
func(1)
func("alex")
func([1,2,3,4])



c#/java
def fun(int arg):
    print(arg)

class A:
    pass
class B(A):
    pass
class C(A):
    pass
#arg为参数，必须是A类型或者A的子类类型
def fun(A arg):
    print(arg)

obj1=B()
func(obj1)