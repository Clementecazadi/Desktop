from ui.all_import_gui import *
from ui.custome.Label import get_font


class Button_custome_1(QPushButton):
    def __init__(self, text='', height=50, minimum_width=50,
                text_padding=55, text_color = '#ffffff', icon_path = '',
                icon_color = '#ffffff', btn_color = '#397e72', btn_hover = '#56c0ac',
                btn_pressed = '#2a5e55', is_active = False, ste = True):
        super(Button_custome_1, self).__init__()
        self.setText(text)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        self.setFont(get_font('JosefinSans-SemiBold.ttf', 14))

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
    def set_active(self, value:bool):
        if value == True or value == False:
            self.is_active = value
            self.apstyle()

    def apstyle(self):
        norlma = f"""
                    QPushButton{{
                        color: {self.text_color};
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
                    padding-left: {self.text_padding}px;
                    text-align: left; 
                    border: none;
                    border-left: 4px solid #fee546;
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
        app_path =abspath(getcwd())
        folder = "ui/icons"
        path = join(app_path, folder)
        image_path = normpath(join(path, image))  
        icon = QPixmap(image_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self.is_active:
            painter.fillRect(icon.rect(), '#8da7e8')
        else:
            painter.fillRect(icon.rect(), color)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height())/2, icon)
        painter.end()


class Button_custome_2(QPushButton):
    def __init__(self, height = 70, width = 70, icon_path = '',
                icon_color = '#ffffff', btn_color = '#9955ff', btn_hover = '#a76cff',
                btn_pressed = '#6c3cb4', is_active = False, border_radius:int = 5, ste = True):
        super(Button_custome_2, self).__init__()
        self.setFixedSize(width, height)
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.my_width = width
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        self.border_radius = border_radius
        if ste:
            self.apstyle()

    def set_active(self, value:bool):
        if value == True or value == False:
            self.is_active = value
            self.apstyle()

    def apstyle(self):
        norlma = f"""
                    QPushButton{{
                        background-color: {self.btn_color};
                        border-radius: {self.border_radius}px;
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
                    background-color: #fee546;
                    border-radius: 5px;
                    border: none;
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
        rect = QRect(0, 0, self.my_width, self.height())
        self.draw_icon(qp, self.icon_path, self.icon_color, rect)
        qp.end()

    def draw_icon(self, qp, image, color, rect):
        app_path =abspath(getcwd())
        folder = "ui/icons"
        path = join(app_path, folder)
        image_path = normpath(join(path, image))  
        icon = QPixmap(image_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        if self.is_active:
            painter.fillRect(icon.rect(), '#397e72')
        else:
            painter.fillRect(icon.rect(), color)
        qp.drawPixmap((rect.width() - icon.width()) / 2, (rect.height() - icon.height())/2, icon)
        painter.end()

class Button_custome_3(QPushButton):
    def __init__(self, text = '1', height = 90, width = 90, btn_color = '#9955ff', 
                btn_hover = '#a76cff', btn_pressed = '#6c3cb4', 
                is_active = False, shortcut='0', font_size = 44, rt:bool = True):
        super(Button_custome_3, self).__init__()
        self.setFixedSize(width, height)
        self.setText(text)
        self.setFont(get_font('JosefinSans-SemiBold.ttf', font_size))
        self.setShortcut(shortcut)
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.width = width
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        self.rt = rt
        self.apstyle()
        

    def set_active(self, value:bool):
        if value == True or value == False:
            self.is_active = value
            self.apstyle()

    def apstyle(self):
        if self.rt:
            norlma = f"""
                        QPushButton{{
                            color: #ffffff;
                            background-color: qlineargradient(spread:pad, x1:0.523, 
                            y1:1, x2:0.514, y2:0, stop:0 rgba(0, 34, 43, 255),
                            stop:1 rgba(55, 200, 171, 255));
                            border-radius: 5px;
                            border: none;
                        }}
                        QPushButton:hover{{
                            background-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.5, y2:1, 
                            stop:0 rgba(169, 113, 255, 255), stop:1 rgba(58, 0, 144, 255));
                        }}
                        QPushButton:pressed{{
                            background-color:  {self.btn_pressed}
                        }}
                    """
        else:
            norlma = f"""
                        QPushButton{{
                            color: #ffffff;
                            background-color: {self.btn_color};
                            border-radius: 5px;
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
                        background-color: #fedb04;
                        border-radius: 5px;
                        border: none;
                }} """ 

        if self.is_active:
            # self.setStyleSheet(norlma + active)
            self.setStyleSheet(active)
        else:
            self.setStyleSheet(norlma)