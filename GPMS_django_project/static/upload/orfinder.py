import os
os.chmod("static/upload/ORFfinder",0o777)
os.system("static/upload/./ORFfinder -in static/upload/test.fa -out static/output/orfoutput.txt")
