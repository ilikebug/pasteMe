#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import asyncio

import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent

    
class ConfigHandler(FileSystemEventHandler):
    '''
    ConfigHandler class
    
    This class is used to handle the configuration file changes.
    '''
    FILENAME = 'config.yml'

    def __init__(self) -> None:
        file_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = f'{file_path}/{self.FILENAME}'

    def on_modified(self, event: FileSystemEvent) -> None:
        if event.src_path == self.filename:
            global conf
            print('Config file changed, reloading..., %s',conf)
            conf = self.load_config()
    
    def load_config(self) -> dict:
        with open(self.filename, 'r') as file:
            return yaml.safe_load(file)

config_handler = ConfigHandler()
conf = config_handler.load_config()

async def init_config() -> None:
    observer = Observer()
    observer.schedule(
        config_handler, 
        path=config_handler.filename, 
        recursive=True
    )
    observer.start()
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        observer.stop()