#!/usr/bin/python2.6
import pexpect
import ptyprocess
import sys
mypassword="kk"
child=pexpect.spawn("passwd xxx")
fout=file('/root/mylog.txt','w')
child.logfile=sys.stdout
child.logfile=fout
child.expect("New password:")
child.sendline(mypassword)
child.expect("Retype new password:")
child.sendline(mypassword)
child.expect("passwd: all authentication")