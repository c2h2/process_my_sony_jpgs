import os
import glob
import subprocess
import PIL.Image
import time



def main():
    start_path = '../'
    files = glob.glob(start_path + '**/*.JPG') ##recursively find all JPG

    print("searching for JPGs")
    for f in files:
        print(f)

    print(str(len(files)) + " files to rename + create resize, hit Ctrl+c to cancel within 5 secs.")
    time.sleep(1); print("5");time.sleep(1);print("4");time.sleep(1);print("3");time.sleep(1);print("2");time.sleep(1);print("1")

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
            cmd = "mkdir -p " + path_new
            output = subprocess.check_output(cmd , shell=True, stderr=subprocess.STDOUT, timeout=300)  
            create_resize(f , 6666, f_new)

        #create thumbnails
        thumbfile = start_path + "/thumbs/thumb_" + os.path.splitext(fn)[0]+".gif"
        cmd = "mkdir -p " + start_path + "/thumbs"
        output = subprocess.check_output(cmd , shell=True, stderr=subprocess.STDOUT, timeout=300)  
        if not os.path.isfile(thumbfile):
            cmd = "convert -auto-orient -define jpeg:size=256x256 "+ f +" -thumbnail 128x128^ -gravity center -extent 128x128 " + thumbfile
            print(cmd)
            output = subprocess.check_output(cmd , shell=True, stderr=subprocess.STDOUT, timeout=300)



def create_resize(f, reso, f_new):
    cmd = "convert " + f + " -resize "+str(reso)+" -quality 85 " + f_new
    if not os.path.isfile(f_new):
        print(cmd)
        output = subprocess.check_output(cmd , shell=True, stderr=subprocess.STDOUT, timeout=300)  


if __name__ == "__main__":
    main()