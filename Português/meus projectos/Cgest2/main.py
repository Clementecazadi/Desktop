from unicodedata import name
from ui.windows.interface import Ui_iterface
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from sys import argv


class MainWindow(QMainWindow,Ui_iterface):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.UI_setup(self)
        self.setMinimumSize(1000, 700)

        # Connectando o click dos botões as funções da animação

        self.menu_burger.clicked.connect(lambda: self.left_menu_animation())
        self.top_user_rigth_frame_simple_view_button.clicked.connect(lambda: self.top_menu_animation())

    def left_menu_animation(self):
        menu_width = self.left_button_frame.width()
        width = 50
        if menu_width == 50: 
            width = 250
        self.LeftMenuAnimation = QPropertyAnimation(self.left_button_frame, b'minimumWidth')
        self.LeftMenuAnimation.setStartValue(menu_width)
        self.LeftMenuAnimation.setEndValue(width)
        self.LeftMenuAnimation.setDuration(500)
        self.LeftMenuAnimation.start()
        self.LeftMenuAnimation.setEasingCurve(QEasingCurve.InOutExpo)
    
    def top_menu_animation(self):
        menu_height = self.top_user_login.height()
        #self.top_user_login.maximumHeight
        height = 100
        if menu_height == 100:
            height = 50
        self.TopMenuAnimation = QPropertyAnimation(self.top_user_login, b'maximumHeight')
        self.TopMenuAnimation.setStartValue(menu_height)
        self.TopMenuAnimation.setEndValue(height)
        self.TopMenuAnimation.setDuration(500)
        self.TopMenuAnimation.start()
        Top_name_animation = QPropertyAnimation(self.top_user_rigth_frame_simple_view_name_user, b'opacity' )
        Top_name_animation.setStartValue(0)
        Top_name_animation.setEndValue(1)
        Top_name_animation.setDuration(500)
        Top_name_animation.start()


app = QApplication(argv)
janela = MainWindow()
janela.show()
app.exec()