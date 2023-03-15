import time
import os
import requests
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "C:\\Users\\beshprakash\\Documents\\Python\\watchdog\\test\\"

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
    url ="http://192.168.178.74:8001/file/"
    def getId(id : int) -> int:
        return id
    def getFileName(filename : str) -> str:

        return filename
    @staticmethod
    def on_any_event(event):
        str2 = "C:\\Users\\beshprakash\\Documents\\Python\\watchdog\\test\\"
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            url = "http://192.168.178.74:8001/file/"
            files = {'file':open(event.src_path,'rb')}
            str1 = event.src_path
            if  str2 in str1:
                str2 = str1.replace(str2,'')
            filename, extension = os.path.splitext(str2) 
            values = {'file_name':filename}
            #requests.post(url, data=values,files=files)

            print("Created data " + filename + " is posted")

        elif event.event_type == 'modified': 
            print(getFileName(str(url)))

            print("Data modified - %s." % event.src_path) 
        elif event.event_type == "deleted":
            print("Data deleted - %s." % event.src_path)
        elif  event.event_type == "moved":

            print("Data moved - %s." % event.src_path)
        elif   event.event_type == "closed":
            print("Data is closed - %s." % event.src_path)
    
   
          

if __name__ == '__main__':
    w = Watcher()
    w.run()