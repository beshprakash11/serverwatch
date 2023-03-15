import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "/home/arrtsm-blackbox2/Documents/detectron2/lengemann/Lengeman/BTLX_final/BTLX_final/progress"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):  
   
    @staticmethod
    def on_any_event(event):
        dst_path = "/home/arrtsm-blackbox2/Documents/mynfs/GCodeServer"
        str2 = "/home/arrtsm-blackbox2/Documents/detectron2/lengemann/Lengeman/BTLX_final/BTLX_final/progress"
        src = "/home/arrtsm-blackbox2/Documents/detectron2/lengemann/Lengeman/BTLX_final/BTLX_final/progress"
        if event.is_directory:
            return None

        elif event.event_type == 'created':            
            print("File is created - %s." %event.src_path)

            str1 = event.src_path
            if  str2 in str1:
                str2 = str1.replace(str2,'')
            filename, extension = os.path.splitext(str2) 
            values = {'file_name':filename}
            src_path = event.src_path
            print("Source: ", src + filename)
            
            print("Destination: ", dst_path)
            shutil.copy(src_path, dst_path)
            try:
                shutil.copy(src_path, dst_path)
            except:
                print("Data format is not valid !!")
            


        elif event.event_type == 'modified': 
            print("Data modified - %s." % event.src_path) 
            str1 = event.src_path
            if  str2 in str1:
                str2 = str1.replace(str2,'')
            filename, extension = os.path.splitext(str2) 
            values = {'file_name':filename}
            src_path = event.src_path
            print("Source: ", src + filename)
            try:
                shutil.copy(src_path, dst_path)
                print("File is modifie successfully.")
            except:
                print("Error to modified files")


            
        elif event.event_type == "deleted":
            print("Data deleted - %s." % event.src_path)
            str1 = event.src_path
            if  str2 in str1:
                str2 = str1.replace(str2,'')
            filename, extension = os.path.splitext(str2) 
            try:
                os.remove(dst_path+str2)
                print("File removed successfully")
            except:
                print("Error to remove files")
            
            
        elif  event.event_type == "moved":
            print("Data moved - %s." % event.src_path)
            str1 = event.src_path
            if  str2 in str1:
                str2 = str1.replace(str2,'')
            filename, extension = os.path.splitext(str2) 
            try:
                os.remove(dst_path+str2)
                print("File moved successfully")
            except:
                print("Error to moved files")
            

        elif   event.event_type == "closed":
            print("Data is closed - %s." % event.src_path)         

if __name__ == '__main__':
    w = Watcher()
    w.run()