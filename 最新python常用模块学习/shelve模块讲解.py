#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import json
li={"1":"2","3":"4"}
h=json.dumps(li)
print(h,type(h))



g=json.loads(h)
print(h,type(g))
