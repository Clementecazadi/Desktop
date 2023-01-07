from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, \
    QProgressBar, QListWidgetItem, QScrollBar, QStackedWidget, QTreeWidget, QTreeWidgetItem,\
    QHeaderView, QGridLayout, QPushButton, QSpacerItem, QListWidget, QMainWindow, QApplication, QLineEdit
from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPainter, QPixmap, QBrush, QImage, QPainter, QWindow, QFontDatabase, QFont
from os.path import abspath, join, normpath
from os import getcwd
from ui.custome.path import path_local 
from ui.custome.circleimage import mask_image
from ui.custome.Label import AdvencedLabel, get_font
from ui.custome.line_edit import AdvencedLine_edit
from ui.custome.button import Button_custome_1, Button_custome_2, Button_custome_3
