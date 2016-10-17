import os
import sys
path=os.path.abspath(__file__)
path=os.path.dirname(os.path.dirname(path))
sys.path.append(path)
os.chdir(path)
from src import student
