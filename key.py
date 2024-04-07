#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import sys

from pynput import keyboard

class KeyboardListener:
    current_keys = set()
    def on_press(self, key, windows):
        self.current_keys.add(key)
        if keyboard.Key.cmd in self.current_keys and \
                key == keyboard.KeyCode.from_char('j'):
            windows.toggle_visibility()

    def on_release(self, key):
        try:
            self.current_keys.remove(key)
        except KeyError:
            pass  
        if key == keyboard.Key.esc:
            sys.exit() 

    def listen_keys(self, windows):
        with keyboard.Listener(
            on_press=lambda event:self.on_press(event, windows),
            on_release=self.on_release) as listener:
            listener.join()
