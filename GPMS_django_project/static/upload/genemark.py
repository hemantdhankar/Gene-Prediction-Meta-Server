import os
import shutil
os.chdir("genemark")
print(os.getcwd())
os.system("./gmst.pl ../test.fa")
shutil.copy('test.fa.lst','../../output')