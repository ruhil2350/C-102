import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCapturObject = cv2.VideoCapture
    result = True
    while(result):
        ret,fame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.iwrite(image_name, fame)
        start_time = time.time
        result = False
    return image_name
    print("snapshot taken")

    videoCapturObject.release()

    cv2.destroyAllWindows()

take_snapshot()

def upload_files(image_name):
    access_token =''
    file = image_name
    file_from = file
    file_to = "/newFolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overWrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 3):
            name = take_snapshot()
            upload_file(name)

main()