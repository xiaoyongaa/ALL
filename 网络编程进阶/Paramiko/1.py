#!/app/python3.5/bin/python3.5
import pexpect
import ptyprocess
child=pexpect.spawn("ssh-copy-id -i /root/.ssh/id_rsa.pub \"root@10.0.0.26\"")
# try:
#     child.expect("The authenticity of host.*")
#     child.sendline("yes")
#     child.sendline("1")
#     # s=child.before.decode()
#     # s1=child.after.decode()
#     # print(s)
#     # print(s1)
# except:
child.sendline("1")
child.expect("[/d].*")
s1=child.after.decode()
print(s1)
    # s=child.before.decode()
    # s1=child.after.decode()
    # print(s)
    # print(s1)
