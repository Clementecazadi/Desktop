from ui.windows.interface import Ui_iterface
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from sys import argv, exit


class MainWindow(QMainWindow, Ui_iterface):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.TopMenuAnimation = None
        self.LeftMenuAnimation = None
        self.UI_setup(self)
        self.setMinimumSize(1280, 700)
        self.setWindowTitle('Cgest, uma nova de gerir o seu restaurante')

        # Connectando o click dos botões as funções da animação
        self.left_button_home.clicked.connect(lambda: self.selection_animation(1))
        self.left_button_caixa.clicked.connect(lambda: self.selection_animation(2))
        self.left_button_mesa.clicked.connect(lambda: self.selection_animation(3))
        self.menu_burger.clicked.connect(lambda: self.left_menu_animation())
        self.top_user_rigth_frame_simple_view_button.clicked.connect(lambda: self.top_menu_animation())

    def selection_animation(self, button_id:int = 0):
        # Recetando todos os botões.
        for btn in self.left_button_frame.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
        if button_id == 1:
            self.left_button_home.set_active(True)
            self.main_cotente.setCurrentIndex(0)
        elif button_id == 2:
            self.left_button_caixa.set_active(True)
            self.main_cotente.setCurrentIndex(1)
        elif button_id == 3:
            self.left_button_mesa.set_active(True)
        
    def left_menu_animation(self):
        menu_width = self.left_button_frame.width()
        width = 50
        icon = 'menu_burger.svg'
        if menu_width == 50:
            width = 250
            icon = 'hide_menu.svg'
        self.LeftMenuAnimation = QPropertyAnimation(self.left_button_frame, b'minimumWidth')
        self.LeftMenuAnimation.setStartValue(menu_width)
        self.LeftMenuAnimation.setEndValue(width)
        self.LeftMenuAnimation.setDuration(500)
        self.menu_burger.icon_path = icon
        self.LeftMenuAnimation.start()
        self.LeftMenuAnimation.setEasingCurve(QEasingCurve.InOutCirc)

    def top_menu_animation(self):
        menu_height = self.top_user_login.height()
        icon = 'hide_user_info.svg'
        height = 100
        show_rigth_element = True
        show_left_element = False
        if menu_height == 100:
            height = 50
            show_rigth_element = False
            show_left_element = True
            icon = 'show_user_info.svg'
        self.TopMenuAnimation = QPropertyAnimation(self.top_user_login, b'maximumHeight')
        self.TopMenuAnimation.setStartValue(menu_height)
        self.TopMenuAnimation.setEndValue(height)
        self.TopMenuAnimation.setDuration(400)
        self.TopMenuAnimation.start()
        self.TopMenuAnimation.setEasingCurve(QEasingCurve.InOutCirc)
        self.top_user_rigth_frame_simple_view_button.icon_path = icon
        self.top_user_rigth_frame_simple_view_name_user.setHidden(show_rigth_element)
        self.top_user_frame_info_lable_name.setHidden(show_left_element)
        self.top_user_frame_info_lable_profil.setHidden(show_left_element)
        self.top_user_frame_info_foto_profil.setHidden(show_left_element)


app = QApplication(argv)
janela = MainWindow()
janela.show()
exit(app.exec())