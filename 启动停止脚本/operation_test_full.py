#!/app/python3.5/bin/python3.5
#脚本名称operation_test_full.py
import os
import sys
JOB_NAME=sys.argv[1]
now_path=str(os.getcwd())
script=str(sys.argv[0]).strip()
script=script.split("/")
script_name=str(script[-1])  #脚本名称
all_list=script_name.split("_")  #脚本的所有字段列表
PROJECT_TYPE="tomcat"  #项目总称字段
PROJECT=str(all_list[0]).strip()  #项目名称字段
ENV_TYPE=str(all_list[1]).strip()  #项目环境类型（测试或者正式）
DEPLOY_TYPE=str(all_list[-1]).strip()
DEPLOY_TYPE=DEPLOY_TYPE.replace(".py","").strip()  #项目部署字段(全量or增量)
JENKINS_HOME=str(os.popen("echo $JENKINS_HOME").read().strip())   #jenkins server程序安装路径
# JAR_WORKSPACE=JENKINS_HOME+"/jobs/"+PROJECT+"_test/workspace/"   #jenkins server下git拉取代码初始路径
# JAR_HOME=JENKINS_HOME+"/jobs/"+PROJECT+"_test/workspace/target/"   #JENKINSwar包总存放点
JAR_WORKSPACE=JENKINS_HOME+"/jobs/"+PROJECT+"_"+ENV_TYPE+"/workspace/"   #jenkins server下git拉取代码初始路径
JAR_HOME=JENKINS_HOME+"/jobs/"+PROJECT+"_"+ENV_TYPE+"/workspace/target/"   #JENKINSwar包总存放点
JAR_NAME=os.popen("find"+" "+JAR_HOME+" "+"-name"+" "+"*.war").read().strip()  #拿到了war包的全路径
workspace_dir=now_path+"/workspace"  #当前脚本的workspace/目录下
tar_dir=workspace_dir+"/tar/"   #tar打包路径
date=os.popen("date +%Y%m%d%H%M%M").read().strip()  #时间戳
tar_name=PROJECT+"_"+date+".tar.gz"  #定义打包名称
#####
# os.system("PROJECT="+PROJECT)
# os.system("tar_name="+tar_name)
# os.system("PROJECT_TYPE="+PROJECT_TYPE)
# os.system("DEPLOY_TYPE="+DEPLOY_TYPE)
# os.system("ENV_TYPE="+ENV_TYPE)
#####

if os.path.exists(tar_dir+PROJECT):
    pass
else:
    os.system("mkdir"+" "+"-p"+" "+tar_dir+PROJECT)
if os.path.exists(JAR_NAME):
    os.system("rm"+" "+"-rf"+" "+tar_dir+PROJECT+"/*")
    os.system("rm"+" "+"-rf"+" "+tar_dir+"*.tar.gz")
    print(JAR_NAME)
    print(tar_dir+PROJECT)
    os.system("cp"+" "+"-r"+" "+JAR_NAME+" "+tar_dir+PROJECT+"/"+PROJECT+".war")
else:
    print("jenkins 代码没有编译好！！")

os.system("cd"+" "+tar_dir+" "+"&&"+" "+"tar"+" "+"-zcf"+" "+tar_name+" "+PROJECT)

if os.path.exists(tar_dir+tar_name):
    os.system("rsync -vzrtopg --progress --delete"+" "+tar_dir+tar_name+" "+"rsync@10.139.113.82::upload --password-file=/etc/rsyncd_jenkins.secrets")
else:
    msg="{path}tar包不存在，打包错误".format(path=tar_dir+tar_name)
    print(msg)



PROJECT=str(PROJECT)
tar_name=str(tar_name)
PROJECT_TYPE=str(PROJECT_TYPE)
DEPLOY_TYPE=str(DEPLOY_TYPE)
ENV_TYPE=str(ENV_TYPE)
args="{project:%s,tar_name:%s,project_type:%s,deploy_type:%s,env_type:%s}"%(PROJECT,tar_name,PROJECT_TYPE,DEPLOY_TYPE,ENV_TYPE)
# os.system("/usr/bin/python2.4 /app/deploy/console/main.py"+args)
#args=args.strip()
# print(args)
# args={"project":PROJECT,"tar_name":tar_name,"project_type":PROJECT_TYPE,"deploy_type":DEPLOY_TYPE,"env_type":ENV_TYPE}
args=str(args).strip()
print(args)
os.system("/usr/bin/python2.4 /app/deploy/console/main.py"+args)
# args={'project':PROJECT,'tar_name':tar_name,'project_type':PROJECT_TYPE,'deploy_type':DEPLOY_TYPE,'env_type':ENV_TYPE}
# print(args)
#args="{'project':'operation','tar_name':'operation_20161025232929.tar.gz','project_type':'tomcat','deploy_type':'full','env_type':'test'}"
# os.system("args=`echo {\'project\':\'$PROJECT\'\,\'tar_name\':\'${tar_name}\'\,\'project_type\':\'${PROJECT_TYPE}\'\,\'deploy_type\':\'${DEPLOY_TYPE}\'\,\'env_type\':\'${ENV_TYPE}\'}`")
# reslut=os.popen("echo $args").read()
# print(reslut)
# os.system("/usr/bin/python2.4 /app/deploy/console/main.py $args")




msg="代码安全扫描报告:  http://jenkins.bangdao-tech.com/report/{w}.html".format(w=JOB_NAME)
print(msg)





