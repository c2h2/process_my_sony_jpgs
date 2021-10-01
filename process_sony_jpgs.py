import os
import glob
import subprocess
import PIL.Image

# set search path and glob for files
# here we want to look for csv files in the input directory
path = '../../favs2'
files = glob.glob(path + '/*.JPG')

def create_resize(f, reso, f_new):
    path = os.path.dirname(os.path.realpath(f))
    fn = os.path.basename(f)

    
    cmd = "mkdir -p " + path_new
    output = subprocess.check_output(cmd , shell=True, stderr=subprocess.STDOUT, timeout=300)  
    cmd2 = "convert " + f + " -resize "+str(reso)+" -quality 85 " + f_new
    if not os.path.isfile(f_new):
        print(cmd2)
        output2 = subprocess.check_output(cmd2 , shell=True, stderr=subprocess.STDOUT, timeout=300)  



for f in files:
    path = os.path.dirname(os.path.realpath(f))
    fn = os.path.basename(f)

    #rename file to dt_based
    img = PIL.Image.open(f)
    exif_taken_dt = img._getexif()[36867]

    if not fn.startswith("20"): #not yet renamed
        new_dt = "-".join(exif_taken_dt.split(" ")[0].split(":"))
        fn_new = path + "/" +new_dt+"_"+fn
        cmd = "mv "+ f + " " + fn_new
        print(cmd)
        output = subprocess.check_output(cmd , shell=True, stderr=subprocess.STDOUT, timeout=300)
        f = fn_new
        fn = os.path.basename(f) 
        path = os.path.dirname(os.path.realpath(f))
                
    #if size > 9.9MB, resize
    size_mb = os.path.getsize(f)/1024/1024
    if size_mb > 9.9:
        path_new = path + "/SMALLED"
        f_new = path_new + "/small_" + fn
        create_resize(f , 6666, f_new)
