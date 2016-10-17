import sys
import os
#sys.exit("sd")

def jingdu(i,max):
    shu=i/max
    shu=int(shu*max)
    shu="\r{du}>{shu}%".format(du="#"*i,shu=shu)
    #print(shu)
    sys.stdout.write(shu)
    sys.stdout.flush()


def main():
    for i in range(0,101):
        jingdu(i,100)

main()