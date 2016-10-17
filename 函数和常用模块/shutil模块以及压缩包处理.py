import shutil
import os
import zipfile
import tarfile
#递归的去拷贝文件夹
#shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
#os.mkdir("rrr")
#shutil.rmtree("rrr")   #删除目录或者文件
#zip压缩
#z=zipfile.ZipFile("test.zip","w")
#z.write("db")   #可以指定压缩文件
#z.write("rrr")  #可以指定压缩目录
#z.close()
#zip解压
#z=zipfile.ZipFile("test.zip","r")
#for i in z.namelist():
    #print(i)
#print(type(z))
#z.extract("rrr/")
#z.close()


#tar包压缩
#tar=tarfile.open("test.tar","w")
#tar.add("db.txt",arcname='bbs2.log')
#tar.close()

#tar包解压
tar=tarfile.open("test.tar","r")
y=tar.getmembers()
obj=tar.getmember("bbs2.log")   #取出对象
print(obj,y)
tar.extract(obj)
tar.close()
