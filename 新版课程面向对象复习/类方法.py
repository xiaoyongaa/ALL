#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong

class f():
    n="x"
    @classmethod
    def g(cls):
        print(cls.n)
    def h(self):
        print(f.n)

    @property
    def p(self,p):
        print(self.n)
    @p.setter
    def p(self,d):
        print(self.n,d)




obj=f()
# obj.g()
# obj.h()
obj.p=1

