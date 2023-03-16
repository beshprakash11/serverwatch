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
            """Check if file exist in destination directory"""
            if os.path.isdir(os.path.join(src_1, dst_path + '/gcode')):
                print('Directoy already exist')
            if os.path.exists(dst_path + "/gcode"):
                print("Code alread exit")
            action = "created"
        elif event.event_type == 'modified':
            action = "updated"
        elif event.event_type == 'deleted':
            action = "deleted"
        elif event.event_type == 'moved':
            action = "moved"
        else:
            action = "unknown"
        print(f"File {event.src_path} was {action}.")
if __name__ == '__main__':
    w = DirectoryWatcher()
    w.run()