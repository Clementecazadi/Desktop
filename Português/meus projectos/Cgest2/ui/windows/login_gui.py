from ui.all_import_gui import *

class login_gui(QMainWindow):
    lock_value = 0
    user_ok = 0
    def __init__(self):
        super(login_gui, self).__init__()
        self.setFixedSize(900, 600)
        self.setWindowTitle('Entre no seu Cgest 2.0')
        # Adicionando um icone a janela.
        icon = QPixmap(path_local('logov1.png'))
        icon = icon.scaled(45, 45, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setWindowIcon(icon)
        
        # Criando o frame principal 
        self.main_frame = QFrame(self)
        self.setCentralWidget(self.main_frame)
        self.main_layout = QHBoxLayout(self.main_frame)
        self.main_layout.setContentsMargins(0, 0 , 0, 0)
        self.main_layout.setSpacing(0)

        self.left_frame = QFrame()
        self.left_frame.setFixedSize(360, 600)
        self.left_frame.setStyleSheet('background-color: #d5ffe6')
        self.left_frame_title = AdvencedLabel('Login', 'berkshire.ttf', 44, '#37c8ab')
        self.left_frame_title.setAlignment(Qt.AlignCenter)
        self.left_frame_user_image = QLabel()
        self.user_image = mask_image('clemente.jpg', 121)
        self.left_frame_user_image.setPixmap(self.user_image)
        self.left_frame_user_image.setAlignment(Qt.AlignCenter)
        self.left_frame_name_user = AdvencedLine_edit('Nome do usuário.', font_size=16)
        self.left_frame_password_user = AdvencedLine_edit('Sua senha.', font_size=16)
        self.left_frame_password_user.setEchoMode(QLineEdit.Password)
        self.left_frame_password_button = Button_custome_2(50, 50, icon_path = 'icon_lock.svg')
        # -----
        self.left_frame_password_layout = QHBoxLayout()
        self.left_frame_password_layout.setSpacing(10)
        self.left_frame_password_layout.addWidget(self.left_frame_password_user)
        self.left_frame_password_layout.addWidget(self.left_frame_password_button)

        self.left_frame_user_login = Button_custome_3('Entrar', rt=False, height=50, width=200,font_size=18)
        self.left_frame_user_login_layout = QHBoxLayout()
        self.left_frame_user_login_layout.addWidget(self.left_frame_user_login)
        # -------
        self.left_frame_user_form_layout = QVBoxLayout()
        self.left_frame_user_form_layout.setContentsMargins(40, 0, 40, 0)
        self.left_frame_user_form_layout.setSpacing(20)
        self.left_frame_user_form_layout.addWidget(self.left_frame_user_image)
        self.left_frame_user_form_layout.addWidget(self.left_frame_name_user)
        self.left_frame_user_form_layout.addLayout(self.left_frame_password_layout)
        self.left_frame_user_form_layout.addLayout(self.left_frame_user_login_layout)

        self.left_frame_forget_password = Button_custome_2(60, 60, border_radius=30, icon_path='forget_password.svg')
        self.left_frame_add_user = Button_custome_2(60, 60, border_radius=30, icon_path='add_user.svg')
        
        
        self.left_frame_more_layout = QHBoxLayout()
        self.left_frame_more_layout.addWidget(self.left_frame_forget_password)
        self.left_frame_more_layout.addWidget(self.left_frame_add_user)

        self.left_frame_spacer1 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.left_frame_spacer2 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.left_frame_layout = QVBoxLayout(self.left_frame)
        self.left_frame_layout.setContentsMargins(0, 15, 0, 25)
        self.left_frame_layout.addWidget(self.left_frame_title)
        self.left_frame_layout.addItem(self.left_frame_spacer1)
        self.left_frame_layout.addLayout(self.left_frame_user_form_layout)
        self.left_frame_layout.addItem(self.left_frame_spacer2)
        self.left_frame_layout.addLayout(self.left_frame_more_layout)
        

        self.right_label = QLabel()
        self.right_image = QPixmap(path_local('login_gui.png'))
        self.right_label.setPixmap(self.right_image)

        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.right_label)

        self.left_frame_password_button.clicked.connect(lambda: self.lock_mode())

    def lock_mode(self):
        if self.lock_value == 0:
            self.left_frame_password_user.setEchoMode(QLineEdit.EchoMode.Normal)
            self.lock_value = 1
            self.left_frame_password_button.icon_path = 'icon_unlock.svg'
        else:
            self.left_frame_password_user.setEchoMode(QLineEdit.EchoMode.Password)
            self.lock_value = 0
            self.user_ok = 1
            self.left_frame_password_button.icon_path = 'icon_lock.svg'

        self.left_frame_password_button.update()
        

  
        