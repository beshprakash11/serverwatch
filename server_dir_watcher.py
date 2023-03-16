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
        src_path1 = "./watch_dir/src/"
        src_path2 = "./watch_dir/src/"
        dst_path = "./watch_dir/dst/"
        if event.is_directory:
            """Check if file exist in destination directory"""
            contents = os.listdir(src_path1)
            for item in contents:
                if os.path.isdir(os.path.join(src_path1, item)):
                    """GCode section"""
                    if os.path.isdir(os.path.join(src_path1, item + "/gcode")):
                        print("Gcode Exist")
                    if os.path.exists(dst_path + item + "/gcode"):
                        print("Code alread exit")
                    else:
                        src_path_gcode = os.path.join(src_path1, item + "/gcode")
                        dst_path_gcode = os.path.join(dst_path, item + "/gcode")
                        shutil.copytree(src_path_gcode, dst_path_gcode)
                        print("GCode copy completed")

                    """Suction cups"""
                    if os.path.exists(dst_path + item + "/suction_cups"):
                        print("Suction cup exist")
                    else:
                        src_path_scup = os.path.join(src_path1, item + "/suction_cups")
                        dst_path_scup = os.path.join(dst_path, item + "/suction_cups")
                        shutil.copytree(src_path_scup, dst_path_scup)
                        print("SCup copy completed")
            
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