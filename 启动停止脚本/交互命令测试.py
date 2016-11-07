#!/app/python3.5/bin/python3.5

#!/app/python3.5/bin/python3.5
import pexpect
import ptyprocess
mypassword="1"
child=pexpect.spawn("passwd xxx")
child.sendline(mypassword)
child.sendline(mypassword)
child.expect("[/d].*")
s=child.before.decode()
s1=child.after.decode()
print(s)
print(s1)


'''
更改用户 xxx 的密码 。
新的 密码：
无效的密码： WAY 过短
无效的密码： 是回文
重新输入新的 密码：
passw
d： 所有的身份验证令牌已经成功更新。
'''
