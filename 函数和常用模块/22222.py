
JAR_WORKSPACE=JENKINS_HOME+"/jobs/"+PROJECT+"_"+ENV_TYPE+"/workspace/"   #jenkins server下git拉取代码初始路径
JAR_HOME=JENKINS_HOME+"/jobs/"+PROJECT+"_"+ENV_TYPE+"/workspace/target/"   #JENKINSwar包总存放点



{'env_type': 'test', 'deploy_type': 'full', 'project_type': 'tomcat', 'tar_name': 'operation_20161025230000.tar.gz', 'project': 'operation'}


{'project':'operation','tar_name':'operation_20161025230202.tar.gz','project_type':'tomcat','deploy_type':'full','env_type':'test'}
{'project_type': 'tomcat', 'deploy_type': 'full', 'tar_name': 'operation_20161025230606.tar.gz', 'env_type': 'test', 'project': 'operation'}



args=echo {\'project\':\'$PROJECT\'\,\'tar_name\':\'${tar_name}\'\,\'project_type\':\'${PROJECT_TYPE}\'\,\'deploy_type\':\'${DEPLOY_TYPE}\'\,\'env_type\':\'${ENV_TYPE}\'}
echo $args

os.system("echo args=`echo {\'project\':\'$PRO\'\,\'tar_name\':\'${tar_name}\'\,\'project_type\':\'${PROJECT_TYPE}\'\,\'deploy_type\':\'${DEPLOY_TYPE}\'\,\'env_type\':\'${ENV_TYPE}\'}`")