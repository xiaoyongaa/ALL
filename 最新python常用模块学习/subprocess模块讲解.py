#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import subprocess

#执行命令状态码
# res=subprocess.check_call("ipconfig /all",shell=True)
# print(res)

#执行命令结果
# res=subprocess.check_output("ipconfig",shell=True)
# print(res,type(res))
#
# print(str(res,encoding="gbk"))


#
# cmd="ipconfig /all"
# #
# # #复杂的交互式命令
# obj = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#
# # # # obj.stdin.write("123")
# # # # obj.stdin.close()
# # # #
# cmd_out = obj.stdout.read()
# print(cmd_out)
# # obj.stdout.close()
# cmd_error = obj.stderr.read()
# # obj.stderr.close()
#
# print(cmd_error)
#
# #print(cmd_error)