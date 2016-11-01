#!/usr/local/python3.5/bin/python3.5
import pexpect
import ptyprocess
cmd="ss"
child=pexpect.spawn("telnet 10.139.100.23 9309")
child.expect("osgi>")
child.sendline(cmd)
child.expect("Framework.*")
s=child.after.decode()
print(s)

