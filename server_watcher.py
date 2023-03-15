import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


"""
Watch directory, source, and destnation directory
"""

src_1 = "./watch_dir/src/"
src_2 = "./watch_dir/src/"
dst_path = "./watch_dir/dst/"


class Watcher:
    DIRECTORY_TO_WATCH = "./watch_dir/src/"
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
            print("Source: ", src_1 + filename)
            
            print("Destination: ", dst_path)
            shutil.copy(src_path, dst_path)
            try:
                shutil.copy(src_path, dst_path)
            except:
                print("Data format is not valid !!")

if __name__ == '__main__':
    w = Watcher()
    w.run()