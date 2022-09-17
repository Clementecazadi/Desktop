from PySide6.QtWidgets import QPushButton
from ui.custome.Label import get_font
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPixmap
import os


class Button_custome(QPushButton):
    def __init__(self, text = '', height = 50, minimum_width = 50,
                text_padding = 55, text_color = '#ffffff', icon_path = '',
                icon_color = '#ffffff', btn_color = '#397e72', btn_hover = '#56c0ac',
                btn_pressed = '#2a5e55', is_active = False, ste = True):
        super(Button_custome, self).__init__()
        self.setText(text)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        self.setFont(get_font('josefin.ttf', 14))

        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.minimum_width = minimum_width
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        if ste:
            self.apstyle()

    def apstyle(self):
        norlma = f"""
                    QPushButton{{
                        color: {self.text_color};
                        font: 500;
                        background-color: {self.btn_color};
                        padding-left: {self.text_padding}px;
                        text-align: left; 
                        border: none;
                    }}
                    QPushButton:hover{{
                        background-color: {self.btn_hover};
                    }}
                    QPushButton:pressed{{
                        background-color:  {self.btn_pressed}
                    }}
                """
        active = f"""QPushButton{{
                    background-color: #13252c;
                    color: {self.text_color};
                    font: 500;
                    padding-left: {self.text_padding}px;
                    text-align: left; 
                    border: none;
                    border-left: 4px solid #fedb04;
            }} """      
               
        if self.is_active:
            # self.setStyleSheet(norlma + active)
            self.setStyleSheet(active)
        else:
            self.setStyleSheet(norlma)

    def paintEvent(self, event):
        QPushButton.paintEvent(self, event)
        qp = QPainter()
        qp.begin(self) 
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        rect = QRect(0, 0, self.minimum_width, self.height())
        self.draw_icon(qp, self.icon_path, self.icon_color, rect)
        qp.end()

    def draw_icon(self, qp, image, color, rect):
        app_path =os.path.abspath(os.getcwd())
        folder = "ui/icons"
        path = os.path.join(app_path, folder)
        image_path = os.path.normpath(os.path.join(path, image))  
        icon = QPixmap(image_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self.is_active:
            painter.fillRect(icon.rect(), '#8da7e8')
        else:
            painter.fillRect(icon.rect(), color)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height())/2, icon)
        painter.end()
