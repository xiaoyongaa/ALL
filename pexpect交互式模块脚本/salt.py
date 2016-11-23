#!/application/python3.5/bin/python3.5
import os

def create_dir():
    bao_name="redis-3.0.6.tar.gz"
    stat=os.system("salt \"*\" cmd.run \"mkdir -p /root/tools/\"")
    if stat==0:
        stat=os.system("salt '*' cp.get_file salt://zip/"+bao_name+" "+"/root/tools/"+bao_name)
        if stat==0:
            print("success")
            return True
        else:
            exit()
    else:
        exit()



def  install():
    print("now,install")
    os.system("salt \"*\" state.highstate")


def main():
    res=create_dir()
    if res:
        print("download ok!")
        res=install()


main()



