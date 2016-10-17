import sys
import os
d=os.getcwd()
d=d.replace("bin","")
sys.path.append(d)
from src import admin
run=getattr(admin,"run")
run()

