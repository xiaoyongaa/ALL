import os
username1="xiaoyong"   #规定正确的用户名
passworld1="x"          #规定正确的密码
c=1
while True:
    username2=input("请输入用户名：")
    passworld2=input("请输入密码：")
    if os.path.exists("user.txt"):
        agouser=open("user.txt").read()
        if agouser==username2:
            print("你之前已经被锁定了，不能登录")
            break
        else:
            if c<3:
                if username1==username2 and  passworld1==passworld2:
                    print("认证成功，欢迎登录")

                else:
                    c+=1
                    print("认证失败，用户名或者密码错误" )
            else:
                print("次数用完,您已被锁定账户")
                n=open("user.txt","w")
                n.write(username2)
                break
    else:
        if c<3:
            if username1==username2 and  passworld1==passworld2:
                print("认证成功，欢迎登录")

            else:
                c+=1
                print("认证失败，用户名或者密码错误" )
        else:
            print("次数用完,您已被锁定账户")
            n=open("user.txt","w")
            n.write(username2)
            break





