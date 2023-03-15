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