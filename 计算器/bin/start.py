import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
from src import main
if hasattr(main,"run"):
    run=getattr(main,"run")
    run()
else:
    print("没有该模块")