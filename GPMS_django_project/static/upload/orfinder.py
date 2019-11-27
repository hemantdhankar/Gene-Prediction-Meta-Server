import os
import shutil
os.chmod("ORFfinder",0o777)
os.system("./ORFfinder -in test.fa -out orfoutput.txt")
shutil.copy('orfoutput.txt', '../output')