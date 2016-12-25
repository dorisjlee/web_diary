from time import sleep
import glob
import os
import random
os.chdir("/Users/dorislee/Desktop/PersonalProj/")
while (True):
    old_file = random.choice(glob.glob("public_photos/*"))
    os.system("mv {} web_diary/assets/img/main.jpg".format(old_file))
    sleep(18000) # 5 hours
    os.system("mv  web_diary/assets/img/main.jpg {}".format(old_file))
