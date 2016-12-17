#!/application/python3.5/bin/python3.5
# -*- coding:utf-8 -*-
# Author:xiaoyong
import shutil
import zipfile


# shutil.copytree()  #拷贝目录
# shutil.copy()   #拷贝文件


#压缩打包
#shutil.make_archive("F:\\test","zip",root_dir="G:\\test")

# zip=zipfile.ZipFile("F:\\test.zip","w")
# zip.write("F:\\技术支持-刘郑义.docx")
#
# zip.close()


#完美支持
#先打包，再压缩
import  tarfile
tar=tarfile.open("F:\\test.tar","w")
tar.add("F:\\技术支持-刘郑义.docx",arcname="xiaoyong.doc")    #增加打包文件,arcname改名打包名
tar.add("F:\\公司脚本",arcname="dsadsadsa")    #增加打包目录
tar.close()

#shutil.make_archive("F:\\all","zip",root_dir="F:\\test.tar")
# zip=zipfile.ZipFile("F:\\all.zip","w")
# zip.write("F:\\test.tar")
#
# zip.close()