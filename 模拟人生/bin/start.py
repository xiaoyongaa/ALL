import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
os.chdir(path)
from src import ren
if hasattr(ren,"run"):
    run=getattr(ren,"run")
    run()
else:
    try:
        raise Exception("没有该模块")
    except Exception as ex:
        print(ex)