import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DirectoryWatcher:
    DIRECTORY_TO_WATCH = "./watch_dir/src/"
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = DirectoryHandler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()

class DirectoryHandler(FileSystemEventHandler):  
    @staticmethod
    def on_any_event(event):
        src_1 = "./watch_dir/src/"
        src_2 = "./watch_dir/src/"
        dst_path = "./watch_dir/dst/"
        if event.is_directory:
            print("File is created - %s." %event.src_path)
if __name__ == '__main__':
    w = DirectoryWatcher()
    w.run()