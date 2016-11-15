#!/usr/bin/python2.6
import pexpect
import ptyprocess
import sys
import os
log_path="/root/mylog.txt"


chid=pexpect.spawn("fdisk /dev/sdb")
fout=file(log_path,"w")
chid.logfile=fout
chid.expect("Device contains neither a valid")
chid.sendline("n")
chid.expect("Command action")

