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

