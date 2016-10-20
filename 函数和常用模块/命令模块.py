#!/app/python3.5/bin/python3.5
import subprocess
import time
import os
ret=subprocess.call("ipconfig", shell=True)
print(ret)

s=subprocess.check_output("ipconfig",shell=True)   #返回的bytes
result=str(s,encoding="gbk")  #转换成字符串
print(result)
# obj = subprocess.Popen("/usr/bin/yum install telnet",stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# obj.stdin.write("y")
# obj.stdin.close()
#
# cmd_out = obj.stdout.read()
# obj.stdout.close()
# cmd_error = obj.stderr.read()
# obj.stderr.close()
#
# print(cmd_out)
#print(cmd_error)