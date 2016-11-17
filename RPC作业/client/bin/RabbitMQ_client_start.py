import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
from src import RabbitMQ_client
if hasattr(RabbitMQ_client,"main"):
    func=getattr(RabbitMQ_client,"main")
    func()