import psutil

pid_list=psutil.pids()
for i in pid_list:
    p=psutil.Process(i)
    print(p.name(),p.status())


