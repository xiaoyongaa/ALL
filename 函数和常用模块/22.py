PROJECT="p"
tar_name="t"
PROJECT_TYPE="R"
DEPLOY_TYPE="D"
ENV_TYPE="E"
# import json
# #args="{project:%s,tar_name:%s,project_type:%s,deploy_type:%s,env_type:%s}"%(PROJECT,tar_name,PROJECT_TYPE,DEPLOY_TYPE,ENV_TYPE)
# #args=dict(args)
# args={"project":PROJECT,"tar_name":tar_name,"project_type":PROJECT_TYPE,"deploy_type":DEPLOY_TYPE,"env_type":ENV_TYPE}
# print(args)
# #args=str(args)
# print(args)
# args=eval(args)
# print(args)


os.system("echo args=`echo {'project':PROJECT")

# args=print({'project':'operation','tar_name':'operation_20161025232929.tar.gz','project_type':'tomcat','deploy_type':'full','env_type':'test'})
# print(args)

os.system("echo $PROJECT")
os.system("echo $tar_name")
os.system("echo $PROJECT_TYPE")
os.system("echo $DEPLOY_TYPE")
os.system("echo $ENV_TYPE")