import os
os.chdir("geneid/bin")
os.system("./geneid -P ../human.param.Feb_22_2006  ../../test.fa > 1.txt")
os.system("cat 1.txt")
