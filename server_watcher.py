import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


"""
Watch directory, source, and destnation directory
"""
watch_dir = "./watch_dir/src/"
src_1 = "./watch_dir/src/"
src_2 = "./watch_dir/src/"
src_dst = "./watch_dir/dst/"


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
