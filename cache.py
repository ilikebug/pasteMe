#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue

from config import conf


class Cache:
    q = Queue(conf.get("cache_size", 10))

    def __init__(self):
        pass

    def put_data(self, data):
        self.q.put(data)

    def get_data(self):
        return self.q.get()
    
    def get_data_list(self):
        return list(self.q.queue)
