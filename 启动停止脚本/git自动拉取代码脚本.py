#!/app/python3.5/bin/python3.5
import os
import sys
import shutil
projcet="ALL/"
user="xiaoyong/"
class all:
    def cmd(self,version):
        res=os.system("mkdir -p /code/"+user)
        if res==0:
            print("代码目录创建成功")
            os.chdir("/code/"+user)
            res=os.system("git clone https://github.com/xiaoyongaa/ALL.git")
            if res==0:
                msg="代码拉取成功！！！"
                print(msg)
                os.chdir(projcet)
                res=os.system("git checkout"+" "+version)
                if res==0:
                    msg="{name}项目{v}版本代码切换成功！！！".format(name=projcet,v=version)
                    res=os.system("tar -zcvf ALL_"+version+".tar.gz --exclude=.*   *")
                    if res==0:
                        print("代码压缩成功")
                        res=os.system("mv *.tar.gz /code/"+user)
                        if res==0:
                            print("代码移动成功！")
                            shutil.rmtree("/code/"+user+projcet)  #原来代码删除
                            #代码推送模块
                        else:
                            print("代码移动失败！")
                    else:
                        print("代码压缩失败")
                else:
                    print("版本切换失败")
            else:
                print("代码拉取失败")
        else:
            print("代码目录创建失败")



    def main(self):
        try:
           version=sys.argv[1]
           print(version)
           self.cmd(version)
        except Exception as ex:
            print("脚本的第一个版本传承不能为空，请输入版本号")

obj=all()
obj.main()