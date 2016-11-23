#!/application/python3.5/bin/python3.5
import os
class foo:
    def create_dir(self):
        stat=os.system("salt \"*\" cmd.run \"mkdir -p /root/tools/\"")
        if stat==0:
            stat=os.system("salt '*' cp.get_file salt://zip/Python-3.5.2.tgz  /root/tools/Python-3.5.2.tgz")
            if stat==0:
                print("success")
                return True
            else:
                exit()
        else:
            exit()



    def  install(self):
        print("now,install")
        os.system("salt \"*\" state.highstate")


    def main(self):
        res=self.create_dir()
        if res:
            print("download ok!")
            res=self.install()


obj=foo()
obj.main()