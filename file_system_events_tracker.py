import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/shaan/Downloads"
to_dir = "C:/Users/shaan/Desktop/python/dowload"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

       def on_created(self,event):
         print("hey {event.src_path} is created")

       def on_deleted(self,event):
         print("oops! someone deleted {event.src_path}")

       def on_modified(self,event):
         print("someone modified {event.src_path}")

       def on_move(self,event):
         print("someone moved {event.src_path} to {event.dest_path}")

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

try:
  while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
    print("stooped!")
    observer.stop()






