import os
import glob
import subprocess
import PIL.Image

# set search path and glob for files
# here we want to look for csv files in the input directory
path = '.'
files = glob.glob(path + '/*.JPG')

def create_resize(f):
    path = os.path.dirname(os.path.realpath(f))
    fn = os.path.basename(f)
    path_new = path + "/SMALLED"
    f_new = path_new + "/small_" + fn
    cmd = "mkdir -p " + path_new
    output = subprocess.check_output(cmd , shell=True, stderr=subprocess.STDOUT, timeout=300)  
    cmd2 = "convert " + f + " -resize 6000 -quality 85 " + f_new
    if not os.path.isfile(f_new):
        print(cmd2)
        output2 = subprocess.check_output(cmd2 , shell=True, stderr=subprocess.STDOUT, timeout=300)  



for f in files:
    size_mb=os.path.getsize(f)/1024/1024
    img = PIL.Image.open(f)
    print(img._getexif()[36867])
    if size_mb > 9.9:
        create_resize(f)
