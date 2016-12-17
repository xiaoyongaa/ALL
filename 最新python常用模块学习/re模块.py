#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong

import re

s="inet 地址:192.168.12.55 广播:192.168.1.12.255"

result=re.findall(r"(\d.*) ",s)
print(result)
