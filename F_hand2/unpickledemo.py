import pickle
from emp import Emp

fp = open("picklefile.dat" ,"rb")
e =  pickle.load(fp)
fp.close()

print(e)