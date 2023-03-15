import time
import os
import requests
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
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
        DIRECTORY_TO_WATCH = "/home/arrtsm-blackbox2/Documents/detectron2/lengemann/lengaman/BTLX_final/BTLX_final/progress/"
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print ("Received created event - %s." % event.src_path)
            url ="http://192.168.178.74:8001/file/"
            files = {'file':open(event.src_path,'rb')}
            str2 = DIRECTORY_TO_WATCH
            str1 = event.src_path

            if  str2 in str1:
                str2 = str1.replace(str2,'')
            filename, extension = os.path.splitext(str2) 
            values = {'file_name':filename}
            requests.post(url, data=values,files=files)
            print("Created ",filename)
            print("Data posted")

        elif event.event_type == 'modified':        
            files = {'file':open(event.src_path,'rb')}
            str2 = DIRECTORY_TO_WATCH
            str1 = event.src_path

            if  str2 in str1:
                str2 = str1.replace(str2,'')
            filename, extension = os.path.splitext(str2) 
            #search existing files
            url ="http://192.168.178.74:8001/file/?file_name=" +filename
            response = requests.get(url).json()
            
            # file exist len=1
            if(len(response) > 0):
                fId  = (json.loads((requests.get(url).text)))[0]['id']
                url ="http://192.168.178.74:8001/file/"+str(fId)+"/"
                print(url)
                values = {'file_name':filename}
                requests.put(url,data = values,files=files)
            else:
                print("There is no existing files!!") 
            print(filename)    
            print("Data Updated")

if __name__ == '__main__':
    w = Watcher()
    w.run()
