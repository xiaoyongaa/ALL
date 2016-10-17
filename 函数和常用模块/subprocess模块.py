import subprocess
import os
os.chdir()
#call
#执行命令，返回状态码
'''
ret=subprocess.call(["ls", "-l"], shell=False) #输入列表，返回状态码
ret=subprocess.call("ls -l", shell=True) #输入字符串，返回状态码

#执行命令，获取结果
str=subprocess.check_output("ls -l",shell=True) #

#复杂的命令
x=subprocess.Popen("mkdir t",shell=True,cwd="/root/")
'''

#复杂的交互式命令
obj = subprocess.Popen(["passwd 1"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("123")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)