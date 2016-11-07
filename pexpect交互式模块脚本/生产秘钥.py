#!/usr/bin/python2.6
import pexpect
import ptyprocess
import sys
import os
log_path="/root/mylog.txt"

def start():
    try:
        child=pexpect.spawn("ssh-keygen -t rsa")
        fout=file(log_path,"w")
        child.logfile=fout
        child.expect("Enter file in which to save the key")
        child.sendline("")
        child.expect("Enter passphrase",timeout=0.1)
        child.sendcontrol("c")
    except Exception as ex:
        print(ex)
        result=os.system("grep -i \"Overwrite\""+" "+log_path)
        return result

def create_first_key():
    child=pexpect.spawn("ssh-keygen -t rsa")
    fout=file(log_path,"w")
    child.logfile=fout
    child.expect("Enter file in which to save the key")
    child.sendline("")
    child.expect("Enter passphrase")
    child.sendline("")
    child.expect("Enter same passphrase")
    child.sendline("")
    child.expect("Your identification has been saved")


def create_senod_key():
    child=pexpect.spawn("ssh-keygen -t rsa")
    fout=file(log_path,"w")
    child.logfile=fout
    child.expect("Enter file in which to save the key")
    child.sendline("")
    child.expect("Overwrite")
    child.sendline("y")
    child.expect("Enter passphrase")
    child.sendline("")
    child.expect("Enter same passphrase again")
    child.sendline("")
    child.expect("Your identification has been saved")








def main():
    result=start()
    if result==0:
        create_senod_key()
        print 2
    else:
        create_first_key()
        print 1


main()




