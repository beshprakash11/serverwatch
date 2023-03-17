import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DirectoryWatcher:
    DIRECTORY_TO_WATCH = "/home/beshpd/Documents/serverwatch/watch_dir/src"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = DirectoryHandler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class DirectoryHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        src_path1 = "/home/beshpd/Documents/serverwatch/watch_dir/src"
        src_path2 = "/home/beshpd/Documents/serverwatch/watch_dir/src"
        dst_path = "/home/beshpd/Documents/serverwatch/watch_dir/dst"
        contents = os.listdir(src_path1)
        if event.is_directory:
            """Check if file exist in destination directory"""
            for item in contents:
                if os.path.isdir(os.path.join(src_path1, item)):
                    """section"""
                    if os.path.isdir(os.path.join(src_path1, item + "/code")):
                        print("code Exist")
                    if os.path.exists(dst_path + item + "/code"):
                        print("Code alread exit")
                    else:
                        src_path_gcode = os.path.join(src_path1, item + "/code")
                        dst_path_gcode = os.path.join(dst_path, item + "/code")
                        shutil.copytree(src_path_gcode, dst_path_gcode)
                        print("Code copy completed")

                    """cups"""
                    if os.path.exists(dst_path + item + "/cups"):
                        print("Suction cup exist")
                    else:
                        src_path_scup = os.path.join(src_path1, item + "/cups")
                        dst_path_scup = os.path.join(dst_path, item + "/cups")
                        shutil.copytree(src_path_scup, dst_path_scup)
                        print("Cup copy completed")

            action = "code | cups crated"
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
