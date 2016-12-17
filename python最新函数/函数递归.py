#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong

def test(n):
    n=n/2
    if int(n)>0:
        print(n)
        return test(int(n))


test(10)