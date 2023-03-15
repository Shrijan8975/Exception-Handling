import pickle
from emp import Emp

e1 = Emp(101, "Amol", 90000)
fp = open("picklefile.dat" ,"wb")
pickle.dump(e1,fp)

fp.close()