#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import asyncio

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QFrame
)
from PyQt5.QtCore import Qt

import config
from cache import Cache

class SpotlightSearch(QWidget, Cache):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setGeometry(400, 200, 600, 100)  # 设置窗口大小和位置
        self.setWindowTitle('PasteMe')

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建搜索框
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText('Search...')
        self.search_box.textChanged.connect(self.on_search)
        layout.addWidget(self.search_box)

        # 创建搜索结果标签
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        # 设置窗口的主布局
        self.setLayout(layout)

    def on_search(self, text):
        self.result_label.setText(f'搜索内容: {self.get_data_list()}')
    

def init_windows():
    app = QApplication(sys.argv)
    windows = SpotlightSearch()
    windows.show()
    sys.exit(app.exec_())

async def main():
    await asyncio.gather(
        # init config
        config.init_config(),
        # init windows
        init_windows()
    )

if __name__ == '__main__':
    asyncio.run(main())

