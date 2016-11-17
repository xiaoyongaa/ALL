import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)

from src import connect_rabbitmq
if hasattr(connect_rabbitmq,"main"):
    func=getattr(connect_rabbitmq,"main")
    func()
