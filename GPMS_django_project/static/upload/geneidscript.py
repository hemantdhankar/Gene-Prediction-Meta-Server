import os
import shutil
os.chdir("geneid/bin")
os.system("./geneid -P ../human.param.Feb_22_2006  ../../test.fa > geneidoutput.txt")
os.system("cat geneidoutput.txt")
shutil.copy('geneidoutput.txt', '../../../output')
